# Telegram-UserBot

<--><-->
• [Установка Termux и базовых компонентов](https://github.com/MavanBest/Telegram-UserBot/blob/main/README.md#-1-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-termux-%D0%B8-%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D1%85-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%D0%BE%D0%B2) 

### 🔧 1. Установка Termux и базовых компонентов
1. Установите Termux из:
   - [F-Droid]
> https://f-droid.org/packages/com.termux
   - Или Google Play (может быть устаревшей версией но в принцепе не чего страшного)

2. Обновите пакеты:
  
```bash
   pkg update && pkg upgrade -y
   ```

---
В процессе установки будет выведенно 
```bash
The default action is to keep your current version.
*** bash.bashrc (Y/I/N/O/D/Z) [default=N] ?
Progress: [ 72%] [████████████████████▋        ]
   ```

После знака ? нада ввести Y после того как появится 
' ~ $ ' можно вводить следующую команду.

---

3. Установите необходимые зависимости:
  
```bash
   pkg install python git -y
   ```

---

### 📥 2. Установка Python-библиотек
1. Установите pip (если не установлен):
  
```bash
   pkg install python-pip -y
   ```

2. Установите Telethon:
  
```bash
   pip install telethon
   ```


### 🛠 3. Настройка проекта
1. Клонируйте репозиторий (или создайте файлы вручную):
  
```bash
   git clone https://github.com/MavanBest/Telegram-UserBot.git
   cd Telegram-UserBot
   ```

   *(Если создаёте вручную — выполните: mkdir -p userbot/handlers userbot/sessions)*

2. Создайте конфиг:
  
```bash
   nano config.py
   ```

   Вставьте содержимое:
  
```python
   API_ID = 1234567  # Замените на ваш
   API_HASH = 'ваш_api_hash'  # Замените на ваш
   PREFIXES = ['.l', '.tlp', '.c', '.cosmo']
   ```

   Сохраните: Ctrl+O → Enter → Ctrl+X.

---

### 🔑 4. Получение API_ID и API_HASH
1. Перейдите на
> https://my.telegram.org
2. Войдите через ваш аккаунт Telegram
3. Создайте приложение:
   - App title: MyUserBot
   - Short name: userbot
4. Скопируйте API_ID и API_HASH в config.py

---

### 🚀 5. Запуск UserBot'а
1. Перейдите в папку проекта (если не перешли) :
  
```bash
   cd Telegram-UserBot
   ```

2. Запустите бота:
  
```bash
   python main.py
   ```

3. При первом запуске:
   - Введите номер телефона (с кодом страны, например +79991234567)
   - Введите код из Telegram (придёт в виде SMS или уведомления)
   - При запросе пароля (если включена 2FA) — введите его

4. После успешной авторизации появится надпись UserBot запущен!
