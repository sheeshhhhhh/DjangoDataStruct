from django.urls import path
from . import views

urlpatterns = [
    path('sendMessage/', views.sendMessage, name="sendMessage")
]