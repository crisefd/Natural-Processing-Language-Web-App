from django.shortcuts import render

# Create your views here.

def syntactic_ana_view(request):
    return render(request, 'index.html')
