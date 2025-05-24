from aiogram import Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state

router = Router()


@router.message(StateFilter(default_state))
async def start_user(message: types.Message):
    await message.answer(message.text)
