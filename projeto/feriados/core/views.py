from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

def natal(request):
    hoje = date.today()
    if hoje.day == 25 and hoje.month == 12:
        natal = True
    else:
        natal = False
    contexto = {
        'natal':natal,
        'carnaval':False
    }
    return render(request, 'natal.html', contexto)

def tiradentes(request):
    contexto = {
        'tiradentes': False,
    }
    return render(request, 'tiradentes.html', contexto)