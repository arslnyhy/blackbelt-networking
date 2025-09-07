import socket
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

data = {'message': 'hello from client', 'type': 'text'}

message_to_send = json.dumps(data).encode()

message_size = len(message_to_send)

length_prefix = message_size.to_bytes(4, byteorder='big')

client_socket.send(length_prefix)
client_socket.send(message_to_send)

response_from_server = client_socket.recv(1024)
received_data = json.loads(response_from_server.decode())
print(f"Server sent back: {received_data}")
client_socket.close()