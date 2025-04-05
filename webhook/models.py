from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class BotUser(TimeStampedModel):
    user_id = models.BigIntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120 )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "BOT USER"
        verbose_name_plural = "BOT USERS"
        ordering = ["-created_at"]


    def __str__(self):
        return f"{self.name} ({self.username}) - ID: {self.user_id}"