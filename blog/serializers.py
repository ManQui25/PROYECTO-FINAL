from rest_framework import serializers
from .models import Post, Comentario, User, Memoria, Reconciliacion, Noticia

from django.contrib.auth import authenticate
#from django.contrib.auth import get_user_model


#User = get_user_model()


from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "name", "phone_number"]


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """This method is called each time the view calls serializer.save()"""
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if not user:
            raise serializers.ValidationError("Username or password is incorrect")
        if user and user.is_active:
            attrs["user"] = user
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    
class ComentarioSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Serializer anidado para el usuario

    class Meta:
        model = Comentario
        fields = ['id', 'post', 'user', 'content', 'date_created']


class PostSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)  # Serializer anidado para los comentarios

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'date_created', 'comentarios']

class MemoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memoria
        fields = '__all__'

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'

class ReconciliacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reconciliacion
        fields = '__all__'