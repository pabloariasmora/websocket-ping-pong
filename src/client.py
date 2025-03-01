import asyncio
import websockets

async def ping_client():
    async with websockets.connect('ws://localhost:8765') as websocket:
        try:
            while True:
                # Wait for ping from server
                ping = await websocket.ping()
                print("Client: Received ping")
                
                # Send pong response
                await websocket.pong()
                print("Client: Sent pong")
                
                await asyncio.sleep(1)
                
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")

if __name__ == "__main__":
    asyncio.run(ping_client())
