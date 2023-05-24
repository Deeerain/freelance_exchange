from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.utils.translation import gettext_lazy as _


admin.site.site_title = _('Exchange')
admin.site.site_header = _('Administration panel')
admin.site.index_title = _('Exchange administration')

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include('burse.urls', namespace='burse')),
    path('', include('accounts.urls', namespace='accounts')),
    path('replays/', include('replays.urls', namespace='replays')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('offers/', include('offers.urls', namespace='offers')),
    path('chats/', include('chatting.urls', namespace='chatting')),

    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
