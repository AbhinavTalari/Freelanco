from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .views import gettingStarted

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', gettingStarted, name='gettingStarted')
]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns+=[path('__debug__/', include(debug_toolbar.urls))]