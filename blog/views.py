from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comentario, Usuario
from .serializers import PostSerializer, ComentarioSerializer, UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAdminUser]

class ComentarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser]

# Create your views here.
