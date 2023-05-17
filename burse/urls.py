from django.urls import path
from . import views

app_name = 'burse'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('freelancers/', views.Freelancers.as_view(), name='freelancer_list'),
]
