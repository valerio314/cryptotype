import asyncio
import aiomysql
from backend.servers.http_server import run_http
from backend.servers.ws_server import run_websocket
from backend.services.db_manager import DBManager
from backend.services.ws_manager import WSManager
from backend.config.settings import POOL_CONFIG, HTTP_SERVER_CONFIG, WS_SERVER_CONFIG

class CryptotypeApp:
    async def run(self):
        """Main application entry point"""
        print("Starting Cryptotype Application...")
        
        try:
            pool = await aiomysql.create_pool(**POOL_CONFIG)
            db_manager = DBManager(pool)
            ws_manager = WSManager(db_manager)
            
            print("Database pool initialized")
            print("Services initialized")
            print(f"Starting HTTP server on {HTTP_SERVER_CONFIG['host']}:{HTTP_SERVER_CONFIG['port']}")
            print(f"Starting WebSocket server on {WS_SERVER_CONFIG['host']}:{WS_SERVER_CONFIG['port']}")
            
            await asyncio.gather(
                run_websocket(WS_SERVER_CONFIG['host'], WS_SERVER_CONFIG['port'], ws_manager.handler),
                asyncio.to_thread(run_http, HTTP_SERVER_CONFIG['host'], HTTP_SERVER_CONFIG['port'])
            )
            
        except Exception as e:
            print(f"Application error: {e}")
        finally:
            if 'pool' in locals():
                pool.close()
                await pool.wait_closed()
                print("Database pool closed")
            print("Application stopped")