from typing import Any

from aiogram import Router
from aiogram.exceptions import (
    TelegramAPIError,
    TelegramUnauthorizedError,
    TelegramBadRequest,
    TelegramNetworkError,
    TelegramNotFound,
    TelegramConflictError,
    TelegramForbiddenError,
    RestartingTelegram,
    CallbackAnswerException,
    TelegramEntityTooLarge,
    TelegramRetryAfter,
    TelegramMigrateToChat,
    TelegramServerError,
)
from aiogram.handlers import ErrorHandler

from bot.utils.misc.logging import logging

router = Router()


@router.errors()
class MyErrorHandler(ErrorHandler):
    async def handle(self) -> Any:
        """
        Xatoliklar qayd etuvchi handler. Barcha xatoliklarni log qiladi va
        ularni qanday qo'lga olish mumkinligini ko'rsatadi.
        """

        # Xatoliklar uchun log yaratish
        error_mapping = {
            TelegramUnauthorizedError: "Bot tokeni yaroqsiz.",
            TelegramNetworkError: "Telegram tarmog'idagi xatolik.",
            TelegramNotFound: "Suhbat, xabar, foydalanuvchi topilmadi.",
            TelegramConflictError: "Bot tokeni takroran ishlatilmoqda.",
            TelegramForbiddenError: "Bot chatdan chiqarilgan.",
            CallbackAnswerException: "Javob qaytmasligi xatoligi.",
            TelegramMigrateToChat: "Suhbat superguruhga ko'chirildi.",
            TelegramServerError: "Telegram serveridan 5xx xatosi.",
            TelegramAPIError: "Telegram API xatosi.",
            TelegramRetryAfter: "So'rovlar ko'payib ketdi.",
            TelegramEntityTooLarge: "Ma'lumotlar limitdan oshdi.",
            TelegramBadRequest: "So'rov noto'g'ri formatda.",
            RestartingTelegram: "Telegram serverini qayta ishga tushirish.",
        }

        # Xatolikni aniqlash va logga yozish
        for exception_class, message in error_mapping.items():
            if isinstance(self.exception_name, exception_class):
                logging.exception(f"{message}: {self.exception_message} \nUpdate: {self.update}")
                return True

        # Bashqa xatoliklar uchun log
        logging.exception(f'Update: {self.update} \n{self.exception_name}')
        return True
