from aiogram.filters.state import StatesGroup, State


class AdminState(StatesGroup):
    ask_ad_content = State()
