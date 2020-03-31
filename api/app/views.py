from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework import generics
from .models import Categoria, Autor, Libro
from .serializers import CategoriaSerializer, AutorSerializer, LibroSerializer

class CategoriaList(generics.ListCreateAPIView):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer

# listar y add
class AutorList(generics.ListCreateAPIView):
	queryset = Autor.objects.all()
	serializer_class = AutorSerializer

# detalle y eliminar
class AutorDetalle(generics.RetrieveDestroyAPIView):
	queryset = Autor.objects.all()
	serializer_class = AutorSerializer

# listar libro
# class LibroList(APIView):
# 	def get(self, request):
# 		libro = Libro.objects.all()[:20]
# 		data = (libro, many=True).data 
# 		return Response(data)

class LibroList(generics.ListCreateAPIView):
	queryset = Libro.objects.all()
	serializer_class = LibroSerializer

# add libro
class LibroAdd(APIView):

	def post(self, request, format=None):
		serializer = LibroSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


