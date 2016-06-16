from django.conf.urls import url
from .views import *

urlpatterns =[
    url(r'^morpho_app/$', morpho_ana_view, name='morpho_ana_view'),
    url(r'^get_morphological_analysis/$', analysis_view, name='analysis_view'),
]
