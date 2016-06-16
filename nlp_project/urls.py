from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.morpho_app.urls', namespace='morpho_app_urls')),
    url(r'^', include('apps.syntactic_app.urls', namespace="syntactic_app_urls")),
]
