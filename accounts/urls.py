from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('me/', views.ProfileView.as_view(), name='profile'),
    path('me/taks/', views.MyTasksView.as_view(), name='tasks'),
    path('me/replays/', views.MyReplays.as_view(), name='replays'),

    path('signin/', LoginView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('signup/', views.RegistrationView.as_view(), name='signup'),
]
