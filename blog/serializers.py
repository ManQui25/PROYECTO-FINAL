from rest_framework import serializers
from .models import Post, Comentario, Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'edad']


class ComentarioSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer(read_only=True)  # Serializer anidado para el usuario

    class Meta:
        model = Comentario
        fields = ['id', 'post', 'user', 'content', 'date_created']


class PostSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)  # Serializer anidado para los comentarios

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'date_created', 'comentarios']
