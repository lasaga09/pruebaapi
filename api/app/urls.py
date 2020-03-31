
from django.urls import path, include
from .views import CategoriaList, AutorList, AutorDetalle, LibroAdd, LibroList

urlpatterns = [
    path('categorias/', CategoriaList.as_view(), name='categoria_list_add'),
    path('autores/', AutorList.as_view(), name='autor_list_add'),
    path('autores/<int:pk>', AutorDetalle.as_view(), name='autor_detalle_delete'),
    path('libros/add', LibroAdd.as_view(), name='libro_add'),
    path('libros/', LibroList.as_view(), name='libro_list'),
]