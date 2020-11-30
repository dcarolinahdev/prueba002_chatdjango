"""Chats admin classes"""

# Django
from django.contrib import admin

# Models
from chats.models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	"""Message admin"""
	list_display = ('user', 'image_msg', 'message_text')
