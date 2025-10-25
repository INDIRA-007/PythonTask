#Network programming
#TCP/ip
#FTP
#sockets
import socket as sk

server_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
server_socket.bind(("localhost",5555))

server_socket.listen()
print("Server is listening...")
while 1:
    client_socket, addr = server_socket.accept()
    print(f"Client-Server connection established: {addr}")
    message = client_socket.recv()
    print(f"Message: {message}")
    client_socket.send("Message received")
    client_socket.close()



