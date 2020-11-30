"""Users URLS"""

# Django
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# Views
from chats import views

urlpatterns = [
	path(
		route = '',
		view = views.MessageList.as_view(),
		name = 'list'
	),
	path(
		route = 'chats/create',
		view = views.MessageCreate.as_view(),
		name = 'create'
	),
	path(
		route = 'chats/<int:pk>/detail/',
		view = views.MessageDetail.as_view(),
		name = 'detail'
	),
	path(
		route = 'chats/<int:pk>/update/',
		view = views.MessageUpdate.as_view(),
		name = 'update'
	),
	path(
		route = 'chats/<int:pk>/delete',
		view = views.MessageDelete.as_view(),
		name = 'delete'
	),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
