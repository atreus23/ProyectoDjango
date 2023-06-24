from django.shortcuts import render

def inicio(request):
    return render(request, "inicio/inicio.html")

def galeria(request):
    return render(request, "galeria/galeria.html")

def blog(request):
    ...
