from django.shortcuts import render
from .models import Video, Artista
from .serializers import VideoSerializer, ArtistaSerializer
from rest_framework import viewsets

class VideoViewSet(viewsets.ModelViewSet):
	serializer_class = VideoSerializer
	queryset = Video.objects.all()

class ArtistaViewSet(viewsets.ModelViewSet):
	serializer_class = ArtistaSerializer
	queryset = Artista.objects.all()
