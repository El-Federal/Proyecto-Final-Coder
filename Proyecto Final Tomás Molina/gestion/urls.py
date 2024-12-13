from django.urls import path
from . import views

app_name = 'gestion'  # Esto define el espacio de nombres

urlpatterns = [
    path('productos/', views.listar_productos, name='listar_productos'),
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]

