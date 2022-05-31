from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def colaboradores(request):
    return render(request, 'colaboradores.html')

def contato(request):
    return render(request, 'contato.html')