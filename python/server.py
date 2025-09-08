import socket
import threading
import time

KEEP_ALIVE_TIMEOUT = 5  # seconds

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind(('0.0.0.0', 8080))
socket_server.listen()
print(f"Server is listening on 0.0.0.0:8080")

def handle_client(conn, addr):
    conn.settimeout(KEEP_ALIVE_TIMEOUT)
    print(f"Connected to {addr}")
    try:
        while True:
            try:
                request_data = conn.recv(4096).decode()
                if not request_data:
                    print(f"Client {addr} disconnected.")
                    break
                print(f"Raw request from {addr}:\n{request_data}")

                # Parse request line
                request_line = request_data.splitlines()[0]
                method, path, version = request_line.split()

                # Build response
                body = f"<html><body><h1>Hello</h1><p>You requested {path}</p></body></html>"
                response = (
                    "HTTP/1.1 200 OK\r\n"
                    f"Content-Length: {len(body)}\r\n"
                    "Content-Type: text/html\r\n"
                    "Connection: keep-alive\r\n"
                    f"Keep-Alive: timeout={KEEP_ALIVE_TIMEOUT}\r\n"
                    "\r\n"
                    f"{body}"
                )
                conn.sendall(response.encode())

            except socket.timeout:
                print(f"Keep-alive timeout for {addr}. Closing connection.")
                break
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection closed with {addr}")

while True:
    conn, addr = socket_server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.daemon = True
    thread.start()