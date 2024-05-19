from aiogram import Router, types, F
import random

router = Router()

# Работа с сообщениями ........................................................
@router.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply(f'И тебе привет')
    elif 'как дела' in message.text.lower():
        await message.reply(f'Нормально, а у тебя?')
    elif 'как тебя зовут' in message.text.lower():
        await message.reply(random.choice(['ТелеБот', 'Теле-Кот', 'Ме2Дэ3']))
    else:
        await message.reply(random.choice(['Я не понимаю...', 'Моя твоя не понимать...']))
