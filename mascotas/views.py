from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):

    return render(request, 'Inicio.html')

def mision(request):

    return render(request, 'Mision.html')

def productos(request):

    return render(request, 'Productos.html')

def voluntariado(request):

    return render(request, 'Voluntariado.html')

def listaVoluntarios(request):

    return render(request, 'ListaVoluntarios.html')

@login_required
def registroStock(request):
    productos=Producto.objects.all()
    datos={'productos' : productos}
    return render(request, 'registroStock.html', datos)

@login_required
def ingresarProducto(request):
    if request.method=="POST":
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()
            return redirect('registroStock')
    else:
        productoform=ProductoForm()
    return render (request, 'ingresarProducto.html', {'productoform' : productoform})

@login_required
def eliminarProducto(request,id):
    productoEliminado = Producto.objects.get(codigo=id)
    productoEliminado.delete()
    return redirect('registroStock')

@login_required
def modificarProducto(request,id):
    productoModificado = Producto.objects.get(codigo=id)
    datos = {
        'form' : ProductoForm(instance=productoModificado)
    }
    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, instance=productoModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect('registroStock')
    return render(request, 'modificarProducto.html', datos)

def registrar(request):
    data={
        'form' : RegistroUserForm()
    }
    if request.method=="POST":
        formulario=RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(user=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
        data["form"]=formulario
    return render(request, 'registration/registrar.html', data)