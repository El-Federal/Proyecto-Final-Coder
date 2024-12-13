from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skins/', views.listar_skins, name='skins'),  # Ya está, no lo toques
    path('skins/<int:skin_id>/', views.detalle_skin, name='detalle_skin'),  # Agregamos este para el detalle de la skin
    path('about-me/', views.about_me, name='about_me'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('productos/', views.listar_productos, name='listar_productos'),  
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),  
    path('skins/', views.listar_skins, name='listar_skins'),
    path('comprar/<int:producto_id>/', views.comprar_skin, name='comprar_skin'),
]


