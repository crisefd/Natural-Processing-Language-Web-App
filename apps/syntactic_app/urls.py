from django.conf.urls import url
from .views import *

urlpatterns =[
    url(r'^syntactic_app/$', syntactic_ana_view, name='syntactic_ana_view'),
#    url(r'^get_analysis/$', analysis_view, name='analysis_view'),
]
