import json
from aiogram import types
from django.http import HttpRequest, HttpResponse
from bot.loader import bot, dp


async def proceed_update(req: HttpRequest):
    upd = types.Update(**(json.loads(req.body)))
    await dp._process_update(bot, upd)