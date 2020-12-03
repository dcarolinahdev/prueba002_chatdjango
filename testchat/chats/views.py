"""Chat views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
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


class MessageList(LoginRequiredMixin, ListView):
	paginate_by = 3
	model = Message
	# template_name = 'chats/message_list.html'

	def get_context_data(self, **kwargs):
		"""Add users list to context"""
		users = User.objects.all()
		context = super().get_context_data(**kwargs)
		context['users'] = users
		return context

class MessageCreate(LoginRequiredMixin, CreateView):
	model = Message
	# fields = ['user', 'profile', 'image_msg']
	# template_name = 'chats/message_form.html'
	form_class = MessageForm
	success_url = reverse_lazy('chats:list')

	def get_context_data(self, **kwargs):
		"""Add user and profile to context"""
		context = super().get_context_data(**kwargs)
		context['user'] = self.request.user
		context['profile'] = self.request.user.profile
		return context

class MessageDetail(LoginRequiredMixin, DetailView):
	model = Message
	# template_name = 'chats/message_detail.html'

class MessageDelete(LoginRequiredMixin, DeleteView):
	model = Message
	success_url = reverse_lazy('chats:list')
