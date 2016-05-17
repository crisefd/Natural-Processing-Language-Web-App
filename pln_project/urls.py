from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.freeling_app.urls', namespace='freeling')),
]
