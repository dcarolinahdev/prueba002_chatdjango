# -*- coding: utf-8 -*-
"""Chat forms."""

# Django
from django import forms

# Model
from chats.models import Message

class MessageForm(forms.ModelForm):
	"""Message model form."""

	class Meta:
		"""Form settings."""
		model = Message
		fields = ('user', 'profile', 'image_msg')
