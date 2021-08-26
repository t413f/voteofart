from random import randint
from loader import types, bot, dp
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text, Command
from keyboards.default import menu
from utils.db_api import dbcontrol

@dp.message_handler(commands=['menu'])
async def show_menu(message: Message):
    await message.answer(text='Используйте меню', reply_markup=menu.menu)

@dp.message_handler(Text(equals=['Случайная картина']))
async def get_art(message: Message):
    current_item = dbcontrol.mydb.get_elem(randint(1, 496))
    photo = types.InputFile(current_item[2])
    await bot.send_message(message.from_user.id, current_item[1])
    await bot.send_photo(message.from_user.id, photo=photo)

@dp.message_handler(Text(equals=['Информация']))
async def get_info(message: Message):
    await bot.send_message(message.from_user.id, text='Данный бот создан исключительно для помощи в прокрастинации!')