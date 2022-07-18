from django.urls import path

from . import views

urlpatterns = [
    path('messages', views.get_messages),
    path('new-message', views.create_message),
]
