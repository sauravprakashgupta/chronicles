from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'admin/', admin.site.urls),
    url(r'^about/$',views.about),
    url(r'^$',views.homepage),
	url(r'^articles/$',include('articles.urls')),
]

urlpatterns += staticfiles_urlpatterns()
