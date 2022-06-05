from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def colaboradores(request):
    return render(request, 'colaboradores.html')

def contato(request):
    return render(request, 'contato.html')

def minicursos(request):
    return render(request, 'minicursos.html')

def eventos(request):
    return render(request, 'eventos.html')

def projetos(request):
    return render(request, 'projetos.html')