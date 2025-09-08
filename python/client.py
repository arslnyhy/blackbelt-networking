import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

print("Connected to server with keep-alive (5s timeout). Type 'quit' to exit.")

while True:
    user_message = input("Enter a path (like /, /hello) or 'quit' to exit: ")

    if user_message.lower() == 'quit':
        break

    request = (
        f"GET {user_message} HTTP/1.1\r\n"
        "Host: localhost\r\n"
        "Connection: keep-alive\r\n"
        "\r\n"
    )

    client_socket.send(request.encode())

    response = client_socket.recv(4096).decode()
    print("Response from server:")
    print(response)

print("Done. Closing client socket.")
client_socket.close()