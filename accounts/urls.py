from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import RegistrationView, ProfileView, MyTasksView, MyReplays


app_name = 'accounts'

urlpatterns = [
    path('me/', ProfileView.as_view(), name='profile'),
    path('me/taks/', MyTasksView.as_view(), name='tasks'),
    path('me/replays/', MyReplays.as_view(), name='replays'),

    path('signin/', LoginView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('signup/', RegistrationView.as_view(), name='signup'),
]
