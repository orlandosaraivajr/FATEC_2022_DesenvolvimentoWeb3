from django.shortcuts import render
from datetime import date

def natal(request):
    hoje = date.today()
    if hoje.day == 7 and hoje.month == 4:
        natal = True
    else:
        natal = False
    contexto = {
        'natal':natal,
        'carnaval':False
    }
    return render(request, 'natal.html', contexto)