"""Создание клавиатуры"""
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_add = KeyboardButton('Добавить рецепт')                 # Кнопка добавить рецепт
button_lib = KeyboardButton('Посмотреть библиотеку рецептов')  # Кнопка библиотеки рецептов

add_kb = ReplyKeyboardMarkup().add(button_add).add(button_lib)