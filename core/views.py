from django.shortcuts import render, redirect
from .models import Producto
from core.forms import ProductoForm


def home(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request, 'core/home.html', contexto)

def form_producto(request):
    formulario = ProductoForm()

    contexto = {'form': formulario}

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje'] = 'Producto guardado correctamente'

    return render(request, 'core/form_productos.html', contexto)


def form_mod_producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    
    contexto = {'form': ProductoForm(instance=producto)}

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje'] = 'Producto actualizado correctamente'

    return render(request, 'core/form_mod_producto.html', contexto)


def form_del_producto(request, id):
    producto = Producto.objects.get(idProducto=id)

    producto.delete()

    return redirect(to='home')