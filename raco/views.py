from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'raco/index.html')

def sobre(request):
     return render (request, 'raco/sobre.html')

def kit(request):
     return render (request, 'raco/kit.html')

def convite(request):
     return render (request,'raco/convite.html')

def lembranca(request):
     return render (request,'raco/lembranca.html')

def index(request):

    itens = [
        {
            "id": 1,
            "imagem":  'img/urso.png' ,
            "descricao": "Kit Festa 🎈",
        },
        {
            "id": 2,
            "imagem": 'img/conv.png',
            "descricao": "Convites ✉️",
        },
        {
            "id": 3,
            "imagem": 'img/ravio.png',
            "descricao": "Lembrancinhas 🎁",
        },
    ]

    context = {
        "itens": itens,
    }

    return render(request, "raco/index.html", context)
