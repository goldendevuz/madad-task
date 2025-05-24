from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from django.utils.translation import gettext as _

router = Router()


@router.message(F.text == "💳 Muddatli to'lov haqida")
async def feedback_1(message: Message, state: FSMContext):
    await message.answer(
        _(
            "<b>Yangi Imkoniyat! \"Muddatli To‘lov\"</b>\n"
            "<i>IT Kurslarini Endi \"Muddatli To‘lov\" Asosida O‘qing! 🎉</i>\n\n"

            "Madad IT Academy sizga IT mutaxassisi bo‘lish va ishlab to‘lash imkoniyatini taqdim etadi!\n\n"

            "🔹 <b>Boshlang‘ich sarmoyasiz o‘qish!</b>\n"
            "IT kasblaridan o‘zingizga mosini tanlang, o‘qishni tugatib, <b>2 oydan so‘ng</b> to‘lovni boshlang!\n\n"

            "🚀 IT sohasida kelajagingizni qurish uchun hoziroq bizga qo‘shiling\n\n"

            "🔹 <b>Nega bu foydali?</b>\n"
            "✅ IT sohasini moliyaviy to‘siqlarsiz o‘rganishni boshlang\n"
            "✅ O‘qish vaqtida hech qanday to‘lov talab qilmaslik\n"
            "✅ Bitirgach <b>2 oy keyin</b>, qulay to‘lov jadvali asosida xarajatlarni qoplash\n\n"

            "🚀 IT mutaxassisi bo‘lish va kelajagingizni bugun yaratish uchun bizga qo‘shiling!"
        )
    )
