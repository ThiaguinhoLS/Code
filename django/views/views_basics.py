# -*- coding: utf-8 -*-
from django.http import HttpResponse

def index(request):
    'View básica no django não faz nenhuma renderização de template'
    return HttpResponse('<h1>Página inicial</h1>')

def index(request):
    'View básica no django renderizando um template'
    return render(request, 'index.html')


