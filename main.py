import asyncio
from backend.app import CryptotypeApp

async def main():
    app = CryptotypeApp()
    await app.run()

if __name__ == "__main__":
    asyncio.run(main())