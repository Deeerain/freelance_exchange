from django.urls import path
from . import views

app_name = 'burse'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('auth/login/', views.LoginView.as_view(), name='auth'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('auth/registration/', views.RegistrationView.as_view(),
         name='registration'),
    path('freelancers/', views.Freelancers.as_view(), name='freelancer_list'),
]
