from rest_framework import serializers
from .models import Categoria, Libro, Autor

class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Autor
		fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Libro
		fields = '__all__'