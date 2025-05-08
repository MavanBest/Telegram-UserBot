import os
import json
import importlib
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from config import API_ID, API_HASH, PREFIXES

class UserBot:
    def __init__(self):
        self.session_file = "session.json"
        self.session_str = self._load_session()
        self.client = TelegramClient(StringSession(self.session_str), API_ID, API_HASH)
        self.prefixes = PREFIXES
        
    def _load_session(self):
        """Загружает сессию из JSON-файла"""
        if os.path.exists(self.session_file):
            try:
                with open(self.session_file, 'r') as f:
                    return json.load(f).get("session")
            except (json.JSONDecodeError, KeyError):
                return None
        return None

    async def _save_session(self):
        """Сохраняет сессию в JSON-файл"""
        with open(self.session_file, 'w') as f:
            json.dump({"session": self.client.session.save()}, f, indent=2)

    async def load_handlers(self):
        """Динамически загружает обработчики из папки handlers"""
        if not os.path.exists('handlers'):
            os.makedirs('handlers')
            
        handler_files = [
            f for f in os.listdir('handlers') 
            if f.endswith('.py') and not f.startswith('_')
        ]
        
        for file in handler_files:
            try:
                module = importlib.import_module(f'handlers.{file[:-3]}')
                if hasattr(module, 'register'):
                    await module.register(self)
            except Exception as e:
                print(f"Ошибка загрузки {file}: {str(e)}")

    async def start(self):
        """Запускает бота"""
        await self.client.start()
        await self._save_session()  # Сохраняем сессию после авторизации
        print("✅ UserBot запущен!")
        await self.load_handlers()
        await self.client.run_until_disconnected()

if __name__ == '__main__':
    bot = UserBot()
    import asyncio
    asyncio.get_event_loop().run_until_complete(bot.start())
