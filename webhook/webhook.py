import json

from aiogram import types
from django.http import HttpRequest

from bot.loader import bot, dp


async def proceed_update(req: HttpRequest):
    # Validate and create the update object
    update = types.Update.model_validate(json.loads(req.body), context={"bot": bot})
    # Process the update using the dispatcher and include the bot
    await dp.feed_update(bot, update)
