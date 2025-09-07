# Blackbelt Networking

This repository demonstrates fundamental TCP networking capabilities using Python sockets.

## What Are You Capable Of?

This networking implementation showcases the following capabilities:

### Core Networking Features
- **TCP Socket Communication**: Reliable, connection-oriented data transfer
- **Client-Server Architecture**: Demonstrates basic client-server patterns
- **Length-Prefixed Protocol**: Implements a custom protocol with 4-byte message length headers
- **JSON Data Exchange**: Structured data communication using JSON serialization
- **Multi-Client Support**: Server can handle multiple clients sequentially

### Technical Capabilities

#### Server (`server.py`)
- Binds to `0.0.0.0:8080` (accepts connections from any network interface)
- Implements length-prefixed message protocol
- Receives and parses JSON messages
- Echoes received messages back to clients
- Handles client disconnections gracefully
- Provides connection logging and status updates

#### Client (`client.py`)
- Connects to TCP server on localhost:8080
- Sends JSON-formatted messages with proper length prefixes
- Receives and parses server responses
- Demonstrates proper socket cleanup

### Protocol Specification
```
Message Format:
[4-byte length prefix (big-endian)] + [JSON message payload]

Example Flow:
1. Client sends: [0x00, 0x00, 0x00, 0x2A] + {"message": "hello from client", "type": "text"}
2. Server responds: {"status": "success", "echo": "hello from client"}
```

## Usage

### Running the Server
```bash
cd python
python3 server.py
```

### Running the Client
```bash
cd python
python3 client.py
```

## Networking Concepts Demonstrated
- Socket creation and configuration
- TCP bind, listen, accept operations
- Connection handling and cleanup
- Binary data framing (length prefixes)
- JSON serialization/deserialization
- Error handling for network operations
- Basic protocol design principles

This implementation serves as a foundation for understanding TCP networking and can be extended with additional features like concurrent client handling, authentication, encryption, or more complex protocols.