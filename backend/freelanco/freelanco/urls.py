from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from .views import gettingStarted,display404

urlpatterns = [
	path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
	path('', TemplateView.as_view(template_name="home/home.html"),name='home'),
	path('home/', include('product.urls')),
	path('accounts/',include('users.urls')),
	path('accounts/',include('allauth.urls')),
	path('contactus/',TemplateView.as_view(template_name="home/contactus.html"),name='contactus'),
	path('notfound',display404),
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
	import debug_toolbar
	urlpatterns+=[path('__debug__/', include(debug_toolbar.urls))]
