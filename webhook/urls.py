from django.urls import path

from core.config import WEBHOOK_PATH
from .views import BotUserAPIView, FeedbackAPIView, telegram_webhook, get_bot_user, send_latest_google_response

urlpatterns = [
    path('bot-users', BotUserAPIView.as_view(), name='bot-users'),
    path('feedbacks', FeedbackAPIView.as_view(), name='feedbacks'),
    path(WEBHOOK_PATH, telegram_webhook, name='telegram_webhook'),
    path('bot-users/<int:user_id>', get_bot_user, name='get_bot_user'),
    path('api/google-sheet-webhook/', send_latest_google_response, name='google-sheet-webhook'),
]
