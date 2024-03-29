# TCP Sockets with Serverlog
<img src="https://github.com/diegodallabt/tcp_sockets_to_transfer_files/assets/75504417/874cfb7e-e91d-4b47-8029-49f077c5536d" width="400" height="250" />

Implementation of a TCP server and client for sending files with connection logs from the server.

# How to use
<img src="https://github.com/diegodallabt/tcp_sockets_to_transfer_files/assets/75504417/01e725ff-f3ec-4fa2-8261-9f1cd22492ad" width="400" height="250" />

First, you need to clone the repository on your machine, to do this run the following command:

```git clone https://github.com/diegodallabt/tcp_sockets_to_transfer_files.git```

After having the repository cloned on your machine, both in the server and client files, you **add the address to the variable *HOST* and the connection port *PORT***. Furthermore, **create directory named "transfer" for it work**.

Now, you're ready to open the connection on server and connect with client.

```python3 server_tcp.py ```

```python3 client_tcp.py ```

Finally, in the client_tcp.py file you can add the path to the file you want to send and press enter, then the file is sent to the repository's "transfer" folder.
