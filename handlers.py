from aiogram import Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Text
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery

from callback_data import ResortCallbackFactory
from chart import get_picture
from keyboards import start_kb, keyboard_list_resort
from utils import get_top_resort, get_list_resort


async def cmd_start(message: Message):
    await message.answer('Привет, ты можешь посмотреть топ по снегу '
                         'или выбрать ГЛК',
                         reply_markup=start_kb())


async def show_top_resort(call: CallbackQuery):
    try:
        await call.message.edit_text('ТОП 5 ГЛК. \n'
                                     'Оценивается кол-во снега за последние 3 дня и на 5 дней вперед',
                                     reply_markup=keyboard_list_resort(get_top_resort(), col=1))
    except TelegramBadRequest:
        await call.message.answer('ТОП 5 ГЛК. \n'
                                  'Оценивается кол-во снега за последние 3 дня и на 5 дней вперед',
                                  reply_markup=keyboard_list_resort(get_top_resort(), col=1))


async def show_list_resort(call: CallbackQuery):
    try:
        await call.message.edit_text('Выбирай ГЛК.',
                                     reply_markup=keyboard_list_resort(get_list_resort()))
    except TelegramBadRequest:
        await call.message.answer('Выбирай ГЛК.',
                                  reply_markup=keyboard_list_resort(get_list_resort()))


async def show_chart_resort(call: CallbackQuery, callback_data: ResortCallbackFactory):
    resort_name = callback_data.resort_name
    await call.message.answer_photo(await get_picture(resort_name),
                                    reply_markup=start_kb())


def register_routers(router: Router):
    router.message.register(cmd_start, Command(commands="start"))
    router.callback_query.register(show_top_resort, Text(contains='top'))
    router.callback_query.register(show_chart_resort, ResortCallbackFactory.filter())
    router.callback_query.register(show_list_resort, Text(contains='choice_resort'))
