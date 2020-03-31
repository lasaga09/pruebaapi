from django.db import models


class Categoria(models.Model):
	nombre = models.CharField(max_length=100, blank=None)

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		verbose_name_plural = 'Categorias'

class Autor(models.Model):
	nombre = models.CharField(max_length=20, verbose_name='Nombres', blank=None)
	apellido = models.CharField(max_length=25, verbose_name='Apellidos', blank=None)

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		verbose_name_plural = 'Autores'

class Libro(models.Model):
	nombre = models.CharField(max_length=50, blank=None)
	autor =  models.ForeignKey(Autor, on_delete=models.CASCADE)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	
	def __str__(self):
		return '{}'.format(self.nombre)

