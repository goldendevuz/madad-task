from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from asgiref.sync import sync_to_async
from django.utils.translation import gettext as _

from bot.cruds.create import create_feedback
from bot.keyboards.reply.buttons import command_start
from bot.states import FeedbackState
from bot.utils.misc import logging
from bot.utils.translations import with_user_language
from core.config import ADMINS
from webhook.models import BotUser

router = Router()


# Define the async-friendly ORM call
@sync_to_async
def get_user_by_id(user_id):
    return BotUser.objects.get(user_id=user_id)


async def on_startup_notify(bot):
    for admin in ADMINS:
        try:
            await bot.send_message(admin, _("The bot has started."))
        except Exception as err:
            logging.exception(err)


@router.message(F.text == _("📨 Taklif va shikoyatlar uchun"))
@with_user_language
async def feedback_1(message: Message, state: FSMContext):
    await message.answer(_("Xabar matnini yuboring."))
    await state.set_state(FeedbackState.body)


@router.message(FeedbackState.body)
async def feedback_2(message: Message, state: FSMContext, bot):
    # ic()
    user_id = message.from_user.id
    user = await get_user_by_id(user_id)
    # ic(user)
    feedback_data = await create_feedback(
        user=user,
        body=message.text
    )
    # ic(feedback_data)

    # Check if feedback creation was successful
    if feedback_data["is_feedback_created"]:
        # ic("if")
        # Send message to admins
        for admin in ADMINS:
            try:
                await bot.send_message(admin,
                                       f'New feedback from <a href="tg://user?id={message.from_user.id}">{message.from_user.full_name}</a>:\n{message.text}',
                                       parse_mode='HTML')
            except Exception as err:
                logging.exception(err)

        # Notify user about feedback submission
        text = _("Adminga jo'natildi. Fikringiz uchun tashakkur.")
        await message.answer(text, reply_markup=command_start)
    else:
        # Notify user if feedback was not created
        text = _("Xabaringizni jo'natishning iloji bo'lmadi")
        await message.answer(text)

    await state.clear()
