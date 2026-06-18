from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'raco/index.html')

def categoria(request):
     return render (request, 'raco/categoria.html')

def kit(request):
     return render (request, 'raco/kit.html')
 


