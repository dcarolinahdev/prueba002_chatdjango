# -*- coding: utf-8 -*-
"""Chat forms."""

from django import forms

class MessageForm(forms.Form):
	image_msg = forms.ImageField()
