from django.urls import path
from . import views
from .views import auth

app_name = 'burse'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('auth/login/', auth.LoginView.as_view(), name='auth'),
    path('auth/logout/', auth.LogoutView.as_view(), name='logout'),
    path('auth/registration/', auth.RegistrationView.as_view(),
         name='registration'),
    path('freelancers/', views.Freelancers.as_view(), name='freelancer_list'),
]
