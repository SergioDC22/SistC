from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ClienteForm, ImpuestoForm
# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def impuestos(request):
    impuestos = Impuesto.objects.all()
    print(impuestos)
    return render(request, 'impuestos/index.html', {'impuestos': impuestos})


def crear(request):
    formulario = ImpuestoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('impuestos')
    return render(request, 'impuestos/crear.html', {'formulario': formulario})


def editar(request, id):
    impuesto = Impuesto.objects.get(idImpuesto=id)
    formulario = ImpuestoForm(request.POST or None,
                              request.FILES or None, instance=impuesto)

    if formulario.is_valid() and request.POST:
        formulario.save()
    return render(request, 'impuestos/editar.html', {'formulario': formulario})


def eliminar(request, idImpuesto):
    impuesto = Impuesto.objects.get(idImpuesto=idImpuesto)
    impuesto.delete()
    return redirect('impuestos')

# APARTADO CLIENTES


def clientes(request):
    clientes = Cliente.objects.all()
    print(clientes)
    return render(request, 'clientes/index2.html', {'clientes': clientes})


def crearC(request):
    formulario = ClienteForm(request.POST or None,
                            request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/crearC.html', {'formulario': formulario})


def editarC(request, id):
    cliente = Cliente.objects.get(idCli=id)
    formulario = ClienteForm(request.POST or None,
                             request.FILES or None, instance=cliente)

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/editarC.html', {'formulario': formulario})


def eliminarC(request, idCli):
    cliente = Cliente.objects.get(idCli=idCli)

    return redirect('clientes')
