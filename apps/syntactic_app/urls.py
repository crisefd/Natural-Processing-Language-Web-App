from django.conf.urls import url
from .views import *

urlpatterns =[
    url(r'^syntactic_app/$', syntactic_ana_view, name='syntactic_ana_view'),
    url(r'^get_syntactic_analysis/$', analysis_view, name='analysis_view'),
    url(r'^get_raw_text/$', get_raw_text_view, name='get_raw_text_view'),
]
