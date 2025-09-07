#!/usr/bin/env python3
"""
Enhanced Client Example - Demonstrates extended server capabilities
"""

import socket
import json
import time

def send_message(data):
    """Send a message to the server and return the response"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))

    message_to_send = json.dumps(data).encode()
    message_size = len(message_to_send)
    length_prefix = message_size.to_bytes(4, byteorder='big')

    client_socket.send(length_prefix)
    client_socket.send(message_to_send)

    response_from_server = client_socket.recv(1024)
    received_data = json.loads(response_from_server.decode())
    client_socket.close()
    
    return received_data

def demonstrate_capabilities():
    """Demonstrate various server capabilities"""
    print("=== Demonstrating Enhanced Server Capabilities ===\n")
    
    # Test 1: Basic message
    print("1. Basic Message:")
    response = send_message({'message': 'Hello from enhanced client', 'type': 'greeting'})
    print(f"   Response: {response}\n")
    
    # Test 2: Ping command
    print("2. Ping Command:")
    response = send_message({'command': 'ping', 'message': 'ping test'})
    print(f"   Response: {response}\n")
    
    # Test 3: Time command
    print("3. Time Command:")
    response = send_message({'command': 'time', 'message': 'what time is it?'})
    print(f"   Response: {response}\n")
    
    # Test 4: Capabilities query
    print("4. Capabilities Query:")
    response = send_message({'command': 'capabilities', 'message': 'what can you do?'})
    print(f"   Response: {response}\n")
    
    # Test 5: Custom data types
    print("5. Custom Data Types:")
    response = send_message({
        'message': 'Complex data test',
        'type': 'data',
        'user_id': 12345,
        'timestamp': time.time(),
        'data': {'nested': 'object', 'values': [1, 2, 3]}
    })
    print(f"   Response: {response}\n")

if __name__ == "__main__":
    try:
        demonstrate_capabilities()
        print("=== All capabilities demonstrated successfully! ===")
    except ConnectionRefusedError:
        print("Error: Could not connect to server. Make sure server.py is running.")
    except Exception as e:
        print(f"Error: {e}")