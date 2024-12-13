from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto 
from django.contrib import messages  
from .forms import RegistroUsuarioForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Vista para el registro de un nuevo usuario
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario
            messages.success(request, 'Te has registrado correctamente. Ahora puedes iniciar sesión.')  # Mensaje de éxito
            return redirect('login')  # Redirige a la página de login después de registrarse
    else:
        form = RegistroUsuarioForm()  # Si es GET, crea un formulario vacío

    return render(request, 'tienda/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Obtiene el usuario y la contraseña del formulario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Autentica al usuario
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)  # Inicia la sesión del usuario
                messages.success(request, "Inicio de sesión exitoso")  # Mensaje de éxito
                return redirect('home')  # Redirige a la página de inicio
            else:
                messages.error(request, "Credenciales incorrectas")  # Mensaje de error si el login falla
        else:
            messages.error(request, "Formulario no válido")  # Mensaje de error si el formulario no es válido
    else:
        form = AuthenticationForm()  # Si es GET, crea un formulario vacío

    return render(request, 'tienda/login.html', {'form': form})

def home(request):
    return render(request, 'tienda/home.html') 

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/listar_productos.html', {'productos': productos})

def skins(request):
    # Aquí puedes obtener las skins de la base de datos más adelante
    return render(request, 'tienda/skins.html')

def about_me(request):
    return render(request, 'tienda/about_me.html')

def listar_skins(request):
    skins = Producto.objects.filter(es_skin=True)
    return render(request, 'tienda/skins.html', {'skins': skins})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def detalle_skin(request, skin_id):
    skin = get_object_or_404(Producto, id=skin_id)
    return render(request, 'tienda/detalle_skin.html', {'skin': skin})



def comprar_skin(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    return render(request, 'skin_comprada.html', {'producto': producto})
