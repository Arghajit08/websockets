import websockets
import asyncio

async def listen():
    url="ws://127.0.0.1:6000"

    async with websockets.connect(url) as websocket:
        i=0
        while True:
            await websocket.send("Hello World!")
        while True:
            message = await websocket.recv()
            print(message)

asyncio.get_event_loop().run_until_complete(listen())