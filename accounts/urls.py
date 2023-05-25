from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import RegistrationView


app_name = 'accounts'

urlpatterns = [
    path('signin/', LoginView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('signup/', RegistrationView.as_view(), name='signup'),
]
