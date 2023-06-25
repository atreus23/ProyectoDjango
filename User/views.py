from django.shortcuts import render, redirect
from User.models import User
from User.registrof import UserForm, MostrarUsuarios

def inicio(request):
    return render(request, "inicio/inicio.html")

def galeria(request):
    return render(request, "galeria/galeria.html")

def blog(request):
    
    buscador = MostrarUsuarios(request.GET)
    
    if request.method == "POST":
        formulario = UserForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            Usuario = User(name=info['nombre'], lastName=info['apellido'], age=info['edad'], email=info['email'])
            # , password=info['password']
            Usuario.save()
            return redirect('blog')
        else:
            return render(request, 'blog.html', {'formulario': formulario})
            
    formulario = UserForm()
    
    

    if buscador.is_valid():
        nombre_a_buscar = buscador.cleaned_data['nombre']
        listado_de_usuarios = User.objects.filter(name__icontains=nombre_a_buscar)
    
    buscador = MostrarUsuarios()
    return render(request, 'blog/blog.html', {'buscador': buscador, 'users': listado_de_usuarios, 'formulario': formulario})