from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('burse.urls', namespace='burse')),
    path('replays/', include('replays.urls', namespace='replays')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('offers/', include('offers.urls', namespace='offers')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

