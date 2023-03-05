from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callback_data import ResortCallbackFactory


def start_kb():
    buttons = [
        [types.InlineKeyboardButton(text='Топ по снегу', callback_data='top')],
        [types.InlineKeyboardButton(text='Выбрать ГЛК', callback_data='choice_resort')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def keyboard_list_resort(resorts: dict, col=2):
    builder = InlineKeyboardBuilder()
    for n, i in resorts.items():
        builder.button(
            text=f'{n} - ❄️{i}', callback_data=ResortCallbackFactory(resort_name=n, value=i)
        )
    builder.adjust(col)
    return builder.as_markup()
