
from django.conf.urls import url
from .views import *


urlpatterns =[
    url(r'^$', hello_world, name='index'),
]
