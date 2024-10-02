from django.urls import path
from .views import BotUserAPIView, telegram
from core.settings import WEBHOOK_PATH

urlpatterns = [
    path('bot-users', BotUserAPIView.as_view(), name='bot-users'),
    path(WEBHOOK_PATH, telegram, name='webhook'),
]
