from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Случайная картина'),
            KeyboardButton(text='Информация')
        ]
    ],
    resize_keyboard=True
)