import socket
import json

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind(('0.0.0.0', 8080))
socket_server.listen()
print(f"Server is listening on 0.0.0.0:8080")

while True:
    conn, addr = socket_server.accept()
    print(f"Connected to client: {addr}")
    
    length_prefix = b''
    while len(length_prefix) < 4:
        chunk = conn.recv(4 - len(length_prefix))
        if not chunk:
            print(f"Client {addr} disconnected.")
            conn.close()
            break
        length_prefix += chunk

    message_length = int.from_bytes(length_prefix, byteorder='big')

    full_message = b''
    while len(full_message) < message_length:
        chunk = conn.recv(message_length - len(full_message))
        if not chunk:
            print(f"Client {addr} disconnected.")
            conn.close()
            break
        full_message += chunk

    received_data = json.loads(full_message.decode())
    print(f"Received data: {received_data}")
    
    response_data = {'status': 'success', 'echo': received_data['message']}
    sending_data = json.dumps(response_data).encode()
    
    conn.send(sending_data)