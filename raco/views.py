from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'raco/index.html')

def categoria(request):
     return render (request, 'raco/categoria.html')

def kit(request):
     return render (request, 'raco/kit.html')
 

def index(request):

    itens = [
        {
            "id": 1,
            "imagem":  'img/urso.png' ,
            "descricao": "Descrição do item 1",
        },
        {
            "id": 2,
            "imagem": 'img/conv.png',
            "descricao": "convites",
        },
        {
            "id": 3,
            "imagem": 'img/ravio.png',
            "descricao": "Lembrancinhas",
        },
    ]

    context = {
        "itens": itens,
    }

    return render(request, "raco/index.html", context)
