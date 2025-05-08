import os
import json
import getpass
from telethon import TelegramClient
from telethon.sessions import StringSession
from config import API_ID, API_HASH, PREFIXES

class UserBot:
    def __init__(self):
        self.session_file = "session.json"
        self.client = TelegramClient(
            StringSession(self._load_session()),
            API_ID,
            API_HASH
        )

    def _load_session(self):
        """Загружает сессию из файла"""
        if os.path.exists(self.session_file):
            with open(self.session_file, 'r') as f:
                return json.load(f).get("session")
        return None

    async def _save_session(self):
        """Сохраняет сессию в файл"""
        with open(self.session_file, 'w') as f:
            json.dump({"session": self.client.session.save()}, f)

    async def start(self):
        """Авторизация с обработкой 2FA"""
        print("🔒 Запуск авторизации...")
        
        if not await self.client.is_user_authorized():
            phone = input("Введите номер телефона (с кодом страны): ")
            await self.client.start(
                phone,
                password=lambda: getpass.getpass("Введите пароль 2FA: "),
                code_callback=lambda: input("Введите код из Telegram: ")
            )
            await self._save_session()
        
        print("✅ UserBot авторизован и готов к работе!")
        await self.client.run_until_disconnected()

if __name__ == '__main__':
    bot = UserBot()
    import asyncio
    asyncio.get_event_loop().run_until_complete(bot.start())
