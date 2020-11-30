# -*- coding: utf-8 -*-
"""Chat models."""

# Django
from django.db import models
from django.contrib.auth.models import User

# Models
from users.models import Profile

class Message(models.Model):
	"""Message model."""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
	message_text = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	image_msg = models.ImageField(
		upload_to='chats/messages', 
		blank=True, 
		null=True
	)

	def __str__(self):
		"""Return email"""
		return self.user.username + " said something on " + str(self.created)
