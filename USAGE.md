# Usage Guide - Blackbelt Networking

## Quick Start

### 1. Basic Server-Client Test
```bash
# Terminal 1: Start the server
cd python
python3 server.py

# Terminal 2: Run the client
cd python
python3 client.py
```

Expected output:
- Server: Shows connection and received data
- Client: Shows server response

### 2. Capability Demonstration
```bash
cd python
python3 capabilities_demo.py
```

This will show all networking capabilities in action.

## What You Can Do

### Test Different Message Types
Modify `client.py` to send different JSON messages:

```python
# Example variations:
data = {'message': 'Custom message', 'type': 'custom'}
data = {'command': 'status', 'user_id': 123}
data = {'action': 'upload', 'filename': 'test.txt', 'size': 1024}
```

### Extend the Protocol
The current implementation supports any JSON-serializable data:

1. **Add Authentication**
   ```python
   data = {'message': 'secret', 'auth_token': 'abc123'}
   ```

2. **Add Commands**
   ```python
   data = {'command': 'list_files', 'directory': '/home'}
   ```

3. **Add File Transfer Support**
   ```python
   data = {'type': 'file', 'filename': 'data.txt', 'content_base64': '...'}
   ```

### Test Network Scenarios

1. **Multiple Clients**: Run `client.py` multiple times while server is running
2. **Large Messages**: Send JSON with large text content
3. **Rapid Messages**: Send multiple messages in quick succession

## Understanding the Code

### Protocol Flow
1. Client connects to server
2. Client sends 4-byte message length (big-endian)
3. Client sends JSON message
4. Server receives length, then message
5. Server processes and responds
6. Connection closes

### Key Learning Points
- **Socket Programming**: Basic TCP operations
- **Protocol Design**: Length-prefixed messaging
- **Data Serialization**: JSON encoding/decoding
- **Error Handling**: Network connection management
- **Binary Data**: Handling byte order and encoding

This implementation demonstrates core networking concepts that form the foundation for more complex networked applications.