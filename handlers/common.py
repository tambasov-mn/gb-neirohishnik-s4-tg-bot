from aiogram import Router, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards.keyboards import keyboard
#
from utils.random_fox import fox
from utils.weathermap import show_weather_msk
from utils.weathermap import show_weather_spb

import json


router = Router()


# ...
@router.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name} \n это Бот ДОМАШНЯЯ РАБОТА 3. \n Для ознакомления со списком команд бота - команда /help', reply_markup=keyboard)


#
@router.message(Command(commands=['помощь']))
@router.message(Command(commands=['help']))
async def help(message: types.Message):
    await message.answer(f'Полный список команд: \n /help - список команд \n /user - имя пользователя \n /info - информация о боте  \n /say_hello - скажи привет \n /random_num - показать рандомное число \n /prof - выбор курсов \n покажи лису - показать фото лисы \n погода в москве - показать температуру в Москве \n погода в питере - показать температуру в Питере')

#
@router.message(Command(commands=['скажи привет']))
@router.message(Command(commands=['say_hello']))
async def user(message: types.Message):
    await message.answer(f'Привет!!!')

#
@router.message(Command(commands=['пользователь']))
@router.message(Command(commands=['user']))
async def user(message: types.Message):
    print('message - test text')
    await message.answer(f'Имя пользователя: {message.chat.first_name}')


# Добавление команды ..........................................................
@router.message(Command(commands=['инфо']))
@router.message(Command(commands=['info']))
async def info(message: types.Message):
    print('message - test text')
    await message.answer(f'Бот Домашнее Задание 3')


# Добавление функции ..........................................................
@router.message(Command(commands=['рандомное число', 'random_num']))
@router.message(F.text.lower() == 'рандомное число')
async def random_num(message: types.Message):
    number = random.randint(0, 100)
    await message.answer(f'Твое рандомное число: {number}!')


# Покдлючение сторонних сервисов - показать фото лисы .........................
@router.message(F.text.lower() == 'покажи лису')
async def fox_s(message: types.Message):
    img_fox = fox()
    await message.answer('Привет, лови лису')
    await message.answer_photo(img_fox)


# Покдлючение сторонних сервисов - погода в Москве ............................
@router.message(F.text.lower() == 'погода в москве')
async def weather_m(message: types.Message):
    weather_t = show_weather_msk()
    await message.answer(f'Сейчас в Москве: {weather_t} градусов цельсия')


# Покдлючение сторонних сервисов - погода в Питере ............................
@router.message(F.text.lower() == 'погода в питере')
async def weather_s(message: types.Message):
    weather_t = show_weather_spb()
    await message.answer(f'Сейчас в Питере: {weather_t} градусов цельсия')




