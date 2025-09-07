import socket
import json
import time

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
    
    # Enhanced response with additional capabilities
    response_data = {
        'status': 'success', 
        'echo': received_data.get('message', ''),
        'type': received_data.get('type', 'unknown'),
        'server_time': time.time(),
        'message_size': len(full_message),
        'client_addr': str(addr)
    }
    
    # Demonstrate simple command processing capability
    if 'command' in received_data:
        if received_data['command'] == 'ping':
            response_data['pong'] = True
        elif received_data['command'] == 'time':
            response_data['server_timestamp'] = time.ctime()
        elif received_data['command'] == 'capabilities':
            response_data['server_capabilities'] = [
                'json_messaging', 'length_prefixed_protocol', 
                'command_processing', 'connection_logging'
            ]
    
    sending_data = json.dumps(response_data).encode()
    
    conn.send(sending_data)