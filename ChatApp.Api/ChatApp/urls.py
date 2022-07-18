from django.urls import path

from . import views

urlpatterns = [
    path('csrf-token', views.get_csrf_token),
    path('messages', views.get_messages),
    path('new-message', views.create_message),
]
