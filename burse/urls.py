from django.urls import path
from burse import views

app_name = 'burse'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('freelancers/', views.Freelancers.as_view(), name='freelancer_list'),
]
