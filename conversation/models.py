from django.db import models
from django.contrib.auth.models import User
from item.models import Item
# Create your models here.


class Conversation(models.Model):
    item = models.models.ForeignKey(Item, related_name=_("conversations"), on_delete=models.CASCADE)
    members = models.models.ManyToManyField(User, related_name=_("conversations"))
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    class meta:
        ordering = ('-modified_at',)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, relate_name='messages', on_delete=models.CASCADE )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)