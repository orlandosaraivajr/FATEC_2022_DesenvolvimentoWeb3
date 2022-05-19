import re
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from core.models import FeriadoModel
from core.forms import FeriadoForm

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

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html', {'formulario': FeriadoForm()})
    else:
        formulario = FeriadoForm(request.POST)
        if formulario.is_valid():
            dados = formulario.cleaned_data
            FeriadoModel.objects.create(**dados)
            contexto = {'feriado':dados.get('nome')}
            return render(request, 'cadastro_ok.html',contexto)
        else:
            contexto = {'formulario': formulario}
            return render(request, 'cadastro.html', contexto)