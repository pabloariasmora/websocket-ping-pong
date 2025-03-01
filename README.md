# WebSocket Ping/Pong Example

A simple example demonstrating WebSocket ping/pong message exchange using Python's websockets library.

## Requirements
- Python 3.7+
- websockets library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/websocket-ping-pong.git
cd websocket-ping-pong
```
     
2. Create a virtual environment (optional but recommended):
```    
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
     
3. Install dependencies:
    
```
pip install -r requirements.txt
```
     
## Usage

1. Start the server:

```
python src/server.py
```
        
In a separate terminal, start the client:

```
python src/client.py
```
     
## How it Works

- The server sends ping frames every 5 seconds
- The client automatically responds with pong frames
- Both sides print messages to show the ping/pong exchange
- The connection is maintained until either side disconnects

##License

- This project is licensed under the MIT License - see the LICENSE file for details
