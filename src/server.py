import asyncio
import websockets
import time

async def ping_server(websocket):
    try:
        while True:
            # Send ping frame
            print("Server: Sending ping")
            await websocket.ping()
            
            # Wait for pong response
            pong_waiter = await websocket.pong()
            print("Server: Received pong")
            
            # Wait 5 seconds before next ping
            await asyncio.sleep(5)
            
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")

async def main():
    async with websockets.serve(ping_server, "localhost", 8765):
        print("Server started on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
