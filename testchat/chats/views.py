"""Chat views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile
from chats.models import Message

# Forms
from chats.forms import MessageForm


class MessageList(ListView):
	paginate_by = 15
	model = Message
	template_name = 'chats/message_form.html'

class MessageCreate(CreateView):
	model = Message
	fields = ['user', 'image_msg']

class MessageDetail(DetailView):
	model = Message

class MessageUpdate(UpdateView):
	model = Message
	fields = ['user', 'image_msg']

class MessageDelete(DeleteView):
	model = Message
	success_url = reverse_lazy('message-list')

class MessageView(FormView):
	template_name = 'message.html'
	form_class = MessageForm
	success_url = '/thanks/'

	def form_valid(self, form):
		# This method is called when valid form data has been POSTed.
		# It should return an HttpResponse.
		return super().form_valid(form)
