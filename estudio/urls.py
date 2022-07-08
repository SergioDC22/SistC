from django.urls import  path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import  static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('index', views.index, name='index'),
    path('impuestos', views.impuestos, name='impuestos'),
    path('impuestos/crear', views.crear, name='crear'),
    path('impuestos/editar', views.editar, name='editar'),
    path('eliminar/<int:idImpuesto>', views.eliminar, name='eliminar'),
    path('impuestos/editar/<int:id>', views.editar, name='editar'),
    
    path('clientes', views.clientes, name='clientes'),
    path('clientes/crearC', views.crearC, name='crearC'),
    path('clientes/editarC', views.editarC, name='editarC'),
    path('eliminar/<int:idCli>', views.eliminarC, name='eliminarC'),
    path('clientes/editarC/<int:id>', views.editarC, name='editarC'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)