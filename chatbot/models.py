from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Chat_messages(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_text = models.TextField()
    bot_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "chat_messages"