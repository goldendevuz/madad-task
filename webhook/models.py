from django.db import models
from django_extensions.db.models import TimeStampedModel


class BotUser(TimeStampedModel):
    user_id = models.BigIntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    language = models.CharField(max_length=10, default="uz")
    deep_link = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        verbose_name = "BOT USER"
        verbose_name_plural = "BOT USERS"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} ({self.username}) - ID: {self.user_id} - Lang: {self.language}"


class Feedback(TimeStampedModel):
    user = models.ForeignKey(BotUser, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField(max_length=2000)
