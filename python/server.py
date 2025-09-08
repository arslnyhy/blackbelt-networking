import socket
import json
import threading

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind(('0.0.0.0', 8080))
socket_server.listen()
print(f"Server is listening on 0.0.0.0:8080")

def handle_client(conn, addr):
    try:
        while True:
            length_prefix = b''
            while len(length_prefix) < 12:
                chunk = conn.recv(12 - len(length_prefix))
                if not chunk:
                    print(f"Client {addr} disconnected.")
                    return
                length_prefix += chunk

            message_length = int.from_bytes(length_prefix, byteorder='big')

            full_message = b''
            while len(full_message) < message_length:
                chunk = conn.recv(message_length - len(full_message))
                if not chunk:
                    print(f"Client {addr} disconnected.")
                    return
                full_message += chunk

            received_data = json.loads(full_message.decode())
            print(f"Received data from {addr}: {received_data}")
            
            response_data = {'status': 'success', 'echo': received_data['message']}
            sending_data = json.dumps(response_data).encode()
            conn.send(sending_data)
            
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection closed with {addr}")

while True:
    conn, addr = socket_server.accept()
    print(f"Connected to client: {addr}")
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.daemon = True
    thread.start()
