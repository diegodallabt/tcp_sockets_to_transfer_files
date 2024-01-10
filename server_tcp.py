import socket
import os
import datetime
import locale

HOST = 'localhost'
PORT = 57000

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

def open_server(HOST, PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    with open('serverlog.txt', 'a') as log:
            date = datetime.datetime.now()
            format_date = date.strftime('[%d/%m/%Y, %H:%M:%S]')
            log.write(f'{format_date} TCP Server wait connection on {PORT} port...\n')

    print('TCP Server wait connection on %d port...' % (PORT))

    try:
        while True:
            conn, addr = s.accept()
            ip, port = addr
            
            with open('serverlog.txt', 'a') as log:
                date = datetime.datetime.now()
                format_date = date.strftime('[%d/%m/%Y, %H:%M:%S]')
                log.write(f"{format_date} Connected estabilished with {ip}:{port}\n")

            print(f"Connected estabilished with {ip}:{port}")
            
            filename = conn.recv(1024).decode('utf-8')

            if filename:
                conn.send('OK'.encode('utf-8'))

                current_dir = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(current_dir, 'transfer', filename)

                with open(file_path, 'wb') as arq:
                    while True:
                        data = conn.recv(1024)
                        if data == b'FILE_TRANSFER_COMPLETE':
                            break
                        arq.write(data)
                
                with open('serverlog.txt', 'a') as log:
                    date = datetime.datetime.now()
                    format_date = date.strftime('[%d/%m/%Y, %H:%M:%S]')
                    log.write(f'{format_date} File {filename} saved\n')
                    
                print('File receive and saved')

    except KeyboardInterrupt:
        with open('serverlog.txt', 'a') as log:
            date = datetime.datetime.now()
            format_date = date.strftime('[%d/%m/%Y, %H:%M:%S]')
            log.write(f'{format_date} Server closed.\n')
        print('Server closed')

    conn.close()

open_server(HOST, PORT)
