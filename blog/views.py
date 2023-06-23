from django.shortcuts import render
from rest_framework import viewsets, permissions,status
from rest_framework.views import APIView
from .models import User
from .models import Post, Comentario, User, Memoria, Noticia, Reconciliacion
from .serializers import (PostSerializer, ComentarioSerializer, UserSerializer, MemoriaSerializer, ReconciliacionSerializer, NoticiaSerializer, ChangePasswordSerializer, LoginSerializer, RegisterSerializer)
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from knox.models import AuthToken
from rest_framework.generics import DestroyAPIView, GenericAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.contrib.auth import get_user_model


class UserModelViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        register_serializer = self.get_serializer(data=request.data)
        register_serializer.is_valid(raise_exception=True)
        user = register_serializer.save()
        instance, token = AuthToken.objects.create(user)
        message = {
            "user": UserSerializer(user).data,
            "token": token,
            "expiry": instance.expiry.strftime("%d %b %Y %H:%M:%S"),
        }
        return Response(message, status=status.HTTP_201_CREATED)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        login_serializer = self.get_serializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        user = login_serializer.validated_data["user"]
        instance, token = AuthToken.objects.create(user)
        message = {
            "user": UserSerializer(user).data,
            "token": token,
            "expiry": instance.expiry.strftime("%d %b %Y %H:%M:%S"),
        }

        return Response(message, status=status.HTTP_200_OK)


class ChangePasswordUpdateAPIView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = get_user_model()
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.obj = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.obj.check_password(serializer.data.get("old_password")):
                return Response(
                    {"message": "Wrong Password"}, status=status.HTTP_400_BAD_REQUEST
                )

            self.obj.set_password(serializer.data.get("new_password"))
            self.obj.save()
            message = {
                "status": "success",
                "message": "Password updated successfully",
            }
            return Response(message, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDestoyAPIView(DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Establecer el usuario actual en el serializer antes de guardar el comentario
            serializer.save(user=request.user, post_id=kwargs['pk'])

            # Realizar cualquier lógica adicional aquí, si es necesario

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        pk = self.kwargs['pk']  # Obtener el ID del post desde los argumentos de la URL
        comentarios = Comentario.objects.filter(post_id=pk)
        serializer = self.get_serializer(comentarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser]
    def get_permissions(self):
        if self.action == 'create':
            # Requiere autenticación para el método POST
            permission_classes = [permissions.IsAuthenticated]
        else:
            # Permite acceso sin autenticación para otros métodos (GET, PUT, DELETE, etc.)
            permission_classes = []
        return [permission() for permission in permission_classes]
    def list(self, request, *args, **kwargs):
        # Obtener los 10 posts más recientes
        latest_posts = Post.objects.order_by('-date_created')[:10]

        # Serializar los posts
        serializer = self.get_serializer(latest_posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})


@api_view(['GET'])
def categoria_reconciliacion_view(request, reconciliacion):
    reconciliacion = Reconciliacion.objects.all()
    serializer = ReconciliacionSerializer(reconciliacion, many=True)
    posts = serializer.data
    return render(request, 'post/categoria_reconciliacion.html', {'posts': posts})
@api_view(['GET'])
def categoria_memorias_view(request, memorias):
    memorias = Post.objects.filter(category='memorias')
    serializer = MemoriaSerializer(memorias, many=True)
    posts = serializer.data
    return render(request, 'post/categoria_memoria.html', {'posts': posts})
@api_view(['GET'])
def categoria_noticias_view(request, noticias):
    noticias = Noticia.objects.all()
    serializer = NoticiaSerializer(noticias, many=True)
    posts = serializer.data
    return render(request, 'post/categoria_noticias.html', {'posts': posts})

@api_view(['POST'])
@login_required
@permission_required('blog.add_post', raise_exception=True)
def create_post(request):
    serializer = PostSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Create your views here.
