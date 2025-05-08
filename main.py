import os
import importlib
from telethon import TelegramClient, events
from config import API_ID, API_HASH, PREFIXES

class UserBot:
    def __init__(self):
        self.client = TelegramClient('sessions/userbot', API_ID, API_HASH)
        self.prefixes = PREFIXES
        
    async def load_handlers(self):
        handler_files = [f for f in os.listdir('handlers') 
                        if f.endswith('.py') and not f.startswith('_')]
        
        for file in handler_files:
            module = importlib.import_module(f'handlers.{file[:-3]}')
            if hasattr(module, 'register'):
                await module.register(self)
    
    async def start(self):
        await self.client.start()
        print("UserBot запущен!")
        await self.load_handlers()
        await self.client.run_until_disconnected()

if __name__ == '__main__':
    bot = UserBot()
    import asyncio
    asyncio.get_event_loop().run_until_complete(bot.start())
