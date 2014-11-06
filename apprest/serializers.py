from rest_framework import serializers
from .models import Video, Artista

class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video
		fields = ('id', 'cancion', 'disco', 'artista',)

class ArtistaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artista
		fields = ('id', 'nombre', 'integrantes',)
