from telethon import events
from telethon.tl.functions.channels import InviteToChannelRequest, EditBannedRequest
from telethon.tl.types import ChatBannedRights

async def register(bot):
    @bot.client.on(events.NewMessage(pattern=r'\.(l|tlp|c|cosmo)\s+(kik|add)\s+(.*)'))
    async def handler(event):
        prefix = event.pattern_match.group(1)
        command = event.pattern_match.group(2)
        target = event.pattern_match.group(3).strip()
        
        if prefix not in bot.prefixes:
            return
            
        if not await event.get_sender().is_admin:
            await event.reply("❌ Только админы могут использовать эту команду!")
            return
            
        try:
            if command == 'kik':
                user = await get_entity(event, target)
                await event.client(EditBannedRequest(
                    event.chat_id,
                    user,
                    ChatBannedRights(until_date=None, view_messages=True)
                ))
                await event.reply(f"👢 Пользователь {user.first_name} исключен!")
                
            elif command == 'add':
                user = await get_entity(event, target)
                await event.client(InviteToChannelRequest(event.chat_id, [user]))
                await event.reply(f"✅ Пользователь {user.first_name} добавлен!")
                
        except Exception as e:
            await event.reply(f"⚠️ Ошибка: {str(e)}")

async def get_entity(event, target):
    try:
        if target.isdigit():
            return await event.client.get_entity(int(target))
        elif target.startswith('@'):
            return await event.client.get_entity(target)
        elif event.is_reply:
            return await event.get_reply_message().get_sender()
    except:
        raise ValueError("Не удалось найти пользователя/чат")
