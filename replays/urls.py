from django.urls import path
from . import views


app_name = 'replays'

urlpatterns = [
    path('add/', views.ReplayCreateView.as_view(), name='add'),
]