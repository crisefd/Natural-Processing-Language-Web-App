
from django.conf.urls import url
from .views import *


urlpatterns =[
    url(r'^$', home_view, name='home_view'),
    url(r'^morpho_analysis/$', freeling_view, name='freeling_view'),
]
