from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm
from tienda.models import Producto

# Vista para listar todos los productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestion/listar_productos.html', {'productos': productos})

# Vista para agregar un nuevo producto
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'gestion/agregar_producto.html', {'form': form})

# Vista para editar un producto
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'gestion/editar_producto.html', {'form': form, 'producto': producto})

# Vista para eliminar un producto
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'gestion/eliminar_producto.html', {'producto': producto})
