import asyncio
import websockets
import json
from decimal import Decimal
from backend.utils.binance_api import get_coins_data
from backend.services.db_manager import DBManager

class WSManager:

    _COINS_LIST = [
        "btcusdt", "ethusdt", "ltcusdt", "xrpusdt","linkusdt",
        "dotusdt", "bnbusdt", "adausdt", "solusdt", "dogeusdt",
        "avaxusdt", "atomusdt", "nearusdt", "algousdt", "filusdt",
        "icpusdt", "openusdt", "uniusdt", "pepeusdt", "pumpusdt"
    ]

    def __init__(self, db_manager):
        self.db_manager = db_manager

    """ Public Methods """
    async def handler(self, websocket):
        # Invia lista cripto
        coins_list_task = None # Se il try solleva un errore, non viene inizializzate e quindi non utilizzabile nell'except
        try:
            coins_list_task = asyncio.create_task(self.send_coins_list(websocket))
        except Exception as e:
            print(f"Fatal Error task_send_coins_data: {e}")
            coins_list_task.cancel()

        # Invia dati cripto real-time
        coins_data_task = None
        try:
            coins_data_task = asyncio.create_task(self.send_coins_data(websocket))
        except Exception as e:
            print(f"Fatal Error task_send_coins_data: {e}")
            coins_data_task.cancel()

        # Routing messages
        try:
            async for message in websocket:
                data = json.loads(message)
                
                match data:
                    case {"type": "signup"}:
                        username = str(data.user_data["username"])
                        email = str(data.user_data["email"])
                        plain_password = str(data.user_data["password"])
                        
                        response = await self.db_manager.create_account(username,
                                                                        email,
                                                                        plain_password)
                        await websocket.send(json.dumps(response))
                    
                    case {"type": "login"}:
                        email = str(data.user_data["email"])
                        plain_password = str(data.user_data["password"])

                        response = await self.db_manager.login(email, plain_password)
                        await websocket.send(json.dumps(response))

                    case {"type": "deposit"}:
                        portfolio_id = data["portfolio_id"]
                        amount = Decimal(str(data["amount"]))

                        response = await self.db_manager.deposit(portfolio_id, amount)
                        await websocket.send(json.dumps(response))

                    case {"type": "withdraw"}:
                        portfolio_id = data["portfolio_id"]
                        amount = Decimal(str(data["amount"]))

                        response = await self.db_manager.withdraw(portfolio_id, amount)
                        await websocket.send(json.dumps(response))

                    case {"type": "execute_order"}:
                        portfolio_id = data ["portfolio_id"]
                        ticker = data["ticker"]
                        execution_price = Decimal(str(data["execution_price"]))
                        size = Decimal(str(data["size"]))

                        response = await self.db_manager.execute_order(portfolio_id,
                                                                       ticker,
                                                                       execution_price,
                                                                       size)
                        await websocket.send(json.dumps(response))

                    case {"type": "close_position"}:
                        position_id = data["position_id"]

                        response = await self.db_manager.close_position(position_id)
                        await websocket.send(json.dumps(response))

        except websockets.ConnectionClosed:
            print(f"Gracefully Disconnection")
        except Exception as e:
            print(f"Fatal Error handler: {e}")


    """ Private Methods """
    async def send_coins_list(self, websocket):
        coins_list = {
            "type": "coins_list",
            "payload": self._COINS_LIST
        }
        await websocket.send(json.dumps(coins_list))


    async def send_coins_data(self, websocket):
        async for coin_data in get_coins_data(self._COINS_LIST):
            await websocket.send(json.dumps(coin_data))