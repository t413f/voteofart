from loader import dp, bot, types
from time import localtime, time, strftime
from data import config


async def info_bot_on():
    await bot.send_message(chat_id=config.ADMIN_ID, text=f"Бот <b>LisaMono</b> запущен! - {strftime('%d.%m.%Y - %H:%M:%S', localtime(time()))}")



