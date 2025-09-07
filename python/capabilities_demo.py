#!/usr/bin/env python3
"""
Capability Demonstration Script for Blackbelt Networking

This script demonstrates the various networking capabilities of the client-server implementation.
"""

import socket
import json
import time
import threading
import sys
from typing import Dict, Any

def demonstrate_basic_communication():
    """Demonstrate basic client-server communication"""
    print("=== Demonstrating Basic Client-Server Communication ===")
    
    # Create and start server in a thread
    server_thread = threading.Thread(target=run_demo_server, daemon=True)
    server_thread.start()
    
    # Give server time to start
    time.sleep(1)
    
    # Test various message types
    test_messages = [
        {"message": "Hello, Server!", "type": "greeting"},
        {"message": "This is a test message", "type": "test", "timestamp": time.time()},
        {"message": "JSON data exchange works!", "type": "data", "count": 42},
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\nTest {i}: Sending {message}")
        response = send_message_to_server(message)
        print(f"Response: {response}")
        time.sleep(0.5)

def run_demo_server():
    """Run a demo server for capability testing"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind(('localhost', 8081))  # Use different port for demo
        server_socket.listen(1)
        print("Demo server listening on localhost:8081")
        
        while True:
            try:
                conn, addr = server_socket.accept()
                print(f"Demo server: Connected to {addr}")
                
                # Read length prefix
                length_prefix = conn.recv(4)
                if len(length_prefix) < 4:
                    continue
                    
                message_length = int.from_bytes(length_prefix, byteorder='big')
                
                # Read full message
                full_message = b''
                while len(full_message) < message_length:
                    chunk = conn.recv(message_length - len(full_message))
                    if not chunk:
                        break
                    full_message += chunk
                
                # Process message
                received_data = json.loads(full_message.decode())
                print(f"Demo server received: {received_data}")
                
                # Send enhanced response
                response_data = {
                    'status': 'success',
                    'echo': received_data.get('message', ''),
                    'received_type': received_data.get('type', 'unknown'),
                    'server_timestamp': time.time(),
                    'capabilities': ['json_exchange', 'length_prefixed_protocol', 'tcp_reliable_delivery']
                }
                
                response_json = json.dumps(response_data).encode()
                conn.send(response_json)
                conn.close()
                
            except Exception as e:
                print(f"Demo server error: {e}")
                
    except Exception as e:
        print(f"Demo server setup error: {e}")
    finally:
        server_socket.close()

def send_message_to_server(data: Dict[Any, Any]) -> Dict[Any, Any]:
    """Send a message to the demo server and return the response"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect(('localhost', 8081))
        
        # Prepare message
        message = json.dumps(data).encode()
        length_prefix = len(message).to_bytes(4, byteorder='big')
        
        # Send message
        client_socket.send(length_prefix)
        client_socket.send(message)
        
        # Receive response
        response = client_socket.recv(1024)
        return json.loads(response.decode())
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        client_socket.close()

def demonstrate_protocol_features():
    """Demonstrate the protocol's features and capabilities"""
    print("\n=== Demonstrating Protocol Features ===")
    
    print("\n1. Length-Prefixed Messages:")
    print("   - 4-byte big-endian length prefix prevents message fragmentation")
    print("   - Enables reliable message boundaries in TCP stream")
    
    print("\n2. JSON Data Exchange:")
    print("   - Structured data communication")
    print("   - Cross-platform compatibility")
    print("   - Human-readable message format")
    
    print("\n3. TCP Reliability Features:")
    print("   - Connection-oriented communication")
    print("   - Guaranteed delivery and ordering")
    print("   - Error detection and recovery")
    
    print("\n4. Server Capabilities:")
    print("   - Listens on configurable address/port")
    print("   - Handles multiple sequential connections")
    print("   - Graceful error handling and logging")

def demonstrate_extensibility():
    """Show how the code can be extended"""
    print("\n=== Extensibility Capabilities ===")
    
    print("\n1. Protocol Extensions:")
    print("   - Add message types (authentication, file transfer, etc.)")
    print("   - Implement compression or encryption")
    print("   - Add heartbeat/keepalive mechanisms")
    
    print("\n2. Architectural Extensions:")
    print("   - Multi-threaded server for concurrent clients")
    print("   - Connection pooling and persistence")
    print("   - Load balancing and failover")
    
    print("\n3. Application Layer Extensions:")
    print("   - Chat applications")
    print("   - File transfer systems")
    print("   - RPC (Remote Procedure Call) frameworks")
    print("   - Custom protocol implementations")

def main():
    """Main demonstration function"""
    print("Blackbelt Networking - Capability Demonstration")
    print("=" * 50)
    
    try:
        demonstrate_basic_communication()
        demonstrate_protocol_features()
        demonstrate_extensibility()
        
        print("\n" + "=" * 50)
        print("Demonstration complete! The networking implementation shows:")
        print("✓ Reliable TCP communication")
        print("✓ Custom protocol with length prefixes")
        print("✓ JSON data exchange")
        print("✓ Error handling and logging")
        print("✓ Extensible architecture")
        
    except KeyboardInterrupt:
        print("\nDemonstration interrupted by user")
    except Exception as e:
        print(f"Demonstration error: {e}")

if __name__ == "__main__":
    main()