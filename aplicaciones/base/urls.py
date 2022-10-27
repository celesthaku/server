from django.urls import path
from .views import Inicio,Listado,FormularioContacto,DetallePost,Suscribir

urlpatterns = [
    path('',Inicio.as_view(), name = 'index'),
    path('general/',Listado.as_view(),{'nombre_categoria':'General'}, name = 'general'),
    path('laptops/',Listado.as_view(),{'nombre_categoria':'Laptops'}, name = 'laptop'),
    path('tablets/',Listado.as_view(),{'nombre_categoria':'Tablets'}, name = 'tablet'),
    path('celulares/',Listado.as_view(),{'nombre_categoria':'Celulares'}, name = 'celular'),
    path('formulario_contacto/', FormularioContacto.as_view(), name = 'formulario_contacto'),
    path('suscribirse/',Suscribir.as_view(), name = 'suscribirse'),
    path('<slug:slug>/',DetallePost.as_view(), name = 'detalle_post'),
]
