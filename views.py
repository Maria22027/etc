from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

from app.forms import FormuUsuario
from app.models import Usuario

def add_usuario(request):

    formUsuario = FormuUsuario(request.POST or None)
    if request.POST:
        if formUsuario.is_valid():
            formUsuario.save()
            return redirect('app')

    context = {
        'form' : formUsuario
    }
    return render(request,'add_usuario.html',context)

def editar_usuario(request, id_usuario):

    usuario = Usuario.objects.get(id=id_usuario)

    formUsuario = FormuUsuario(request.POST or None, instance=usuario)
    if request.POST:
        if formUsuario.is_valid():
            formUsuario.save()
            return redirect('app')

    context = {
        'form' : formUsuario
    }
    return render(request,'editar_usuario.html',context)

def excluir_usuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.delete()
    return redirect('app')

   
def app(request):

    usuario = Usuario.objects.all()

    dados = {
        'usuarios' : usuario
    }

    pagina = loader.get_template('home.html')
    return HttpResponse(pagina.render(dados))
