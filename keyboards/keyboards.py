# Добавим кнопки в наш проект:
from aiogram import types

#
button1 = types.KeyboardButton(text='/help')
button2 = types.KeyboardButton(text='/user')
button3 = types.KeyboardButton(text='/info')
button4 = types.KeyboardButton(text='/say_hello')
button5 = types.KeyboardButton(text='/random_num')
button6 = types.KeyboardButton(text='/prof')
button7 = types.KeyboardButton(text='Покажи лису')
button8 = types.KeyboardButton(text='Погода в Москве')
button9 = types.KeyboardButton(text='Погода в Питере')

# Ряды кнопок:
kb = [
    [button1, button2, button3],
    [button4, button5, button6],
    [button7, button8, button9]
]

#
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)





