from django.urls import path
from . import views

app_name = 'chatting'

urlpatterns = [
    path('<str:chat_box_name>/', views.chat_box)
]
