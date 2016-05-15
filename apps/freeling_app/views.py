from django.shortcuts import render
from django.template import Template, Context
# from django.http import HttResponse
import freeling
# Create your views here.

def hello_world(request):
    return render(request, 'index.html')
