from aiogram import executor
from loader import dp, bot
from handlers import handlers, menu
import asyncio
from data import config
import aioschedule


async def on_startup():
    await handlers.info_bot_on()

    # await set_default_commands(dispatcher)

    # await on_startup_notify(dispatcher)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, on_startup=on_startup, loop=loop)

