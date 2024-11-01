from django.urls import path
from .views import BotUserAPIView, telegram_webhook, get_bot_user
from core.data.config import WEBHOOK_PATH

urlpatterns = [
    path('bot-users', BotUserAPIView.as_view(), name='bot-users'),
    path(WEBHOOK_PATH, telegram_webhook, name='telegram_webhook'),
    path('bot-users/<int:user_id>', get_bot_user, name='get_bot_user')
]