from aiogram import Router


# from bot.filters import ChatPrivateFilter


def setup_routers() -> Router:
    from .users import admin, start, help, set_lang, feedback, term_payment, courses, services, contact, register, \
        shared
    from .errors import error_handler

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    # start.router.message.filter(ChatPrivateFilter(chat_type=["private"]))

    router.include_routers(start.router, shared.router, admin.router, help.router, error_handler.router,
                           set_lang.router, feedback.router, term_payment.router, courses.router, services.router,
                           contact.router, register.router)

    return router
