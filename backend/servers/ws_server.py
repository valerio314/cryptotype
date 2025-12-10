import asyncio
import websockets

async def run_websocket(ip:str, port:int, handler):
    async with websockets.serve(handler, ip, port):
        print(f"Server WebSocket Online [ws://{ip}:{port}]")
        await asyncio.Future()