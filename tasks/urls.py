from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.TaksListView.as_view(), name='list'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('<slug:slug>/', views.TaksListView.as_view(), name='list_by_category'),
    path('<slug:category_slug>/<slug:slug>/', views.TaskDetailView.as_view(), name='detail'),
]