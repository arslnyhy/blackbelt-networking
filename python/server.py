import socket
import json
import threading

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind(('0.0.0.0', 8080))
socket_server.listen()
print(f"Server is listening on 0.0.0.0:8080")

def handle_client(conn, addr):
    try:
        # 1. Read request
        request_data = conn.recv(1024).decode()
        if not request_data:
            print(f"Client {addr} disconnected.")
            return
        print(f"Raw request from {addr}:\n{request_data}")

        # 2. Parse minimal request line
        request_line = request_data.splitlines()[0]
        method, path, version = request_line.split()

        # 3. Build minimal response
        body = f"<html><body><h1>Hello from minimal HTTP server!</h1><p>You requested {path}</p></body></html>"
        response = (
            "HTTP/1.1 200 OK\r\n"
            f"Content-Length: {len(body)}\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            f"{body}"
        )

        # 4. Send response
        conn.sendall(response.encode())

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
