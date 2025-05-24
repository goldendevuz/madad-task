from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from django.utils.translation import gettext as _

# Importing the services_inline_keyboard from bot.keyboards.inline.buttons
from bot.keyboards.inline.buttons import services_inline_keyboard

router = Router()

# Short default message
DEFAULT_MESSAGE = _("📅 Bizning Xizmatlarimiz:\n\n"
                    "🚀 Sun’iy intellekt (AI) xizmatlari\n"
                    "💻 IT xizmatlari\n"
                    "🎨 Grafik Dizayn va Media xizmatlari\n\n"
                    "👇 Boshqa xizmatlarni ko‘rish uchun quyidagi tugmalarni bosing.")

# Full service descriptions (for detailed view)
AI_SERVICES = _("🔹 Sun’iy intellekt (AI) xizmatlari\n"
                "✅ Chatbot va virtual yordamchilar yaratish (AI chatbotlar, mijozlarga xizmat ko‘rsatish botlari)\n"
                "✅ Matn, rasm va ovozga asoslangan AI yechimlar (NLP, ovozli yordamchilar, avtomatik tarjima)\n"
                "✅ Tahliliy va prognoz AI tizimlari (Ma’lumotlar tahlili, biznes jarayonlarni optimallashtirish)\n"
                "✅ Avtomatlashtirilgan kontent yaratish (AI yordamida matn va dizaynlar yaratish)")

IT_SERVICES = _("🔹 IT xizmatlari\n"
                "✅ Web saytlar yaratish (Veb-saytlar, onlayn do‘konlar, CMS tizimlar)\n"
                "✅ Mobil Ilovalar ishlab chiqish (iOS va Android ilovalar - Flutter, Native)\n"
                "✅ Ma’lumotlar bazasi yechimlari (SQL, Firebase, Big Data tahlili)\n"
                "✅ ERP & CRM tizimlari yaratish (Biznes jarayonlarni avtomatlashtirish)\n"
                "✅ IT Konsalting (Biznesingizga mos IT yechimlar tavsiyasi)")

DESIGN_SERVICES = _("🔹 Grafik Dizayn va Media xizmatlari\n"
                    "✅ Brending va logotip dizayni\n"
                    "✅ SMM uchun post va banner dizayni\n"
                    "✅ Reklama va marketing materiallari (vizitkalar, bukletlar, flyerlar)\n"
                    "✅ Mobilografiya va animatsiya (Video montaj, reklama roliklari, motion dizayn)")

ALL_SERVICES = _(
    "💡 Sizning IT, AI va Dizayn sohasidagi har qanday loyihalaringizni hayotga tatbiq qilishga tayyormiz!"
)


@router.message(F.text == _("📅 IT Xizmatlarimiz"))
async def show_services(message: Message):
    await message.answer(
        DEFAULT_MESSAGE,
        reply_markup=services_inline_keyboard()
    )


@router.callback_query(F.data == "ai_services")
async def show_ai_services(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        _(
            "{services_title}\n\n"
            "{ai_services}"
        ).format(
            services_title=_("🚀 Sun’iy intellekt (AI) xizmatlari"),
            ai_services=AI_SERVICES,
        ),
        reply_markup=services_inline_keyboard()
    )


@router.callback_query(F.data == "it_services")
async def show_it_services(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        _(
            "{services_title}\n\n"
            "{it_services}"
        ).format(
            services_title=_("💻 IT xizmatlari"),
            it_services=IT_SERVICES,
        ),
        reply_markup=services_inline_keyboard()
    )


@router.callback_query(F.data == "design_services")
async def show_design_services(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        _(
            "{services_title}\n\n"
            "{design_services}"
        ).format(
            services_title=_("🎨 Grafik Dizayn va Media xizmatlari"),
            design_services=DESIGN_SERVICES,
        ),
        reply_markup=services_inline_keyboard()
    )


@router.callback_query(F.data == "all_services")
async def show_all_services(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        _(
            "{services_title}\n\n"
            "{ai_services}\n\n"
            "{it_services}\n\n"
            "{design_services}\n\n"
            "<b>💡 Barcha xizmatlarimiz:</b> {all_services}"
        ).format(
            services_title=_("Barcha Xizmatlarimiz"),
            ai_services=AI_SERVICES,
            it_services=IT_SERVICES,
            design_services=DESIGN_SERVICES,
            all_services=ALL_SERVICES,
        ),
        reply_markup=services_inline_keyboard()
    )
