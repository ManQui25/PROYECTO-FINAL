from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comentario, Usuario
from .serializers import PostSerializer, ComentarioSerializer, UsuarioSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecciona a la página de inicio después de iniciar sesión
        else:
            return render(request, 'user/login.html', {'error': 'Credenciales inválidas.'})
    else:
        return render(request, 'user/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirecciona a la página de inicio después de registrar al usuario
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})

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
