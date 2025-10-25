
import socket as sk
client_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
client_socket.connect(("localhost",5555))

client_socket.send("Hello server...")
response = client_socket.recv()
print(f"server says: {response}")

client_socket.close()