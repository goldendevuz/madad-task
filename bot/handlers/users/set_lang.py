from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from asgiref.sync import sync_to_async
from django.utils.translation import activate, gettext as _

from bot.utils import with_user_language, update_google_sheet
from webhook.models import BotUser  # adjust "myapp" to your Django app name

router = Router()

# Define available languages and labels
LANGUAGE_CHOICES = {
    "🇺🇿 Uzbek": "uz",
    "🇷🇺 Russian": "ru",
    "🇺🇸 English": "en",
    "🇩🇪 German": "de",
    "🇸🇦 Arabic": "ar",
}


def get_lang_keyboard():
    buttons = [
        [InlineKeyboardButton(text=label, callback_data=f"setlang:{code}")]
        for label, code in LANGUAGE_CHOICES.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@router.message(F.text == "/setlang")
@with_user_language
async def send_lang_selection(message: types.Message):
    await message.answer(_("Please choose your language:"), reply_markup=get_lang_keyboard())


@sync_to_async
def save_botuser_lang(telegram_id: int, lang_code: str):
    # Get or create the BotUser record based on telegram_id.
    bot_user, _ = BotUser.objects.get_or_create(user_id=telegram_id, defaults={'name': '', 'username': ''})
    bot_user.language = lang_code
    bot_user.save()
    return bot_user.language


@router.callback_query(lambda c: c.data and c.data.startswith("setlang:"))
async def handle_lang_selection(callback: CallbackQuery):
    lang_code = callback.data.split(":")[1]
    telegram_id = callback.from_user.id
    # Save the chosen language in the database.
    await save_botuser_lang(telegram_id, lang_code)
    # Activate the language for Django translations.
    # Although activate() is synchronous and thread-local, it’s fine here since it’s a fast call.
    activate(lang_code)
    # Optionally, if you are sending translated text, ensure you call gettext after activation.
    await callback.message.edit_text(f"Language set to {lang_code.upper()} ✅")
    await callback.answer()
    await update_google_sheet()
