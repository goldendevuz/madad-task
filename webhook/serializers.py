from rest_framework import serializers

from .models import BotUser, Feedback


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = "__all__"

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"