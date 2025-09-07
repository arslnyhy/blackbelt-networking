import socket
import json

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind(('0.0.0.0', 8080))
socket_server.listen()
print(f"Server is listening on 0.0.0.0:8080")

while True:
    conn, addr = socket_server.accept()
    print(f"Connected to client: {addr}")
    while True:
        msg = conn.recv(1024)
        if not msg:
            print(f"Client {addr} disconnected.")
            conn.close()
            break
        
        received_data = json.loads(msg.decode())
        print(f"Received data: {received_data}")
        
        response_data = {'status': 'success', 'echo': received_data['message']}
        
        sending_data = json.dumps(response_data).encode()
        
        conn.send(sending_data)