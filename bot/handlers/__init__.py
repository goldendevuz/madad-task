from aiogram import Router

from bot.filters import ChatPrivateFilter


def setup_routers() -> Router:
    from .users import admin, start, help, echo, set_lang
    from .errors import error_handler

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    start.router.message.filter(ChatPrivateFilter(chat_type=["private"]))

    router.include_routers(admin.router, start.router, help.router, echo.router, error_handler.router, set_lang.router)

    return router
