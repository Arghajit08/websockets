import websockets
import asyncio

PORT=6000

print("Server is running on port", str(PORT))

async def echo(websocket, path):
    print("Client connected")
    try:
        async for message in websocket:
            print("Received:", message)
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosed as e:
        print("Client disconnected")
        return

start_server=websockets.serve(echo, "localhost", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()