import asyncio
import socket
import websockets

clients = set()

async def handler(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            pass  # Handle incoming messages if necessary
    finally:
        clients.remove(websocket)

async def broadcast(message):
    for client in clients:
        await client.send(message)

def listen_e131():
    UDP_IP = "0.0.0.0"
    UDP_PORT = 5568
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        yield data

async def forward_e131_to_websocket():
    for packet in listen_e131():
        dmx_data = packet[126:]
        rgb_values = [dmx_data[i:i+3] for i in range(0, len(dmx_data), 3)]
        message = {"pixels": [{"r": rgb[0], "g": rgb[1], "b": rgb[2]} for rgb in rgb_values]}
        await broadcast(message)

start_server = websockets.serve(handler, "0.0.0.0", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_until_complete(forward_e131_to_websocket())
asyncio.get_event_loop().run_forever()
