from django.db import models

# Create your models here.

class Artista(models.Model):
	nombre = models.TextField(max_length=100)
	integrantes = models.TextField(max_length=100)

class Video(models.Model):
	cancion = models.TextField(max_length=100)
	disco = models.TextField(max_length=100)
	artista = models.ForeignKey(Artista)
	
