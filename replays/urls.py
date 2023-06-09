from django.urls import path
from replays import views


app_name = 'replays'

urlpatterns = [
    path('add/', views.ReplayCreateView.as_view(), name='add'),
]
