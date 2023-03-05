from typing import Optional
from aiogram.filters.callback_data import CallbackData


class ResortCallbackFactory(CallbackData, prefix='resort'):
    resort_name: str
    value: Optional[int]
