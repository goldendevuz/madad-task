from django.urls import path
from .views import BotUserAPIView, telegram_webhook, home_view
from core.settings import WEBHOOK_PATH

urlpatterns = [
    path('', home_view, name='home'),
    path('bot-users', BotUserAPIView.as_view(), name='bot-users'),
    path(WEBHOOK_PATH, telegram_webhook, name='telegram_webhook'),
]
