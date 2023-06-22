"""
URL configuration for proyectofinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from blog.views import UsuarioViewSet, ComentarioViewSet, PostViewSet, login_view, register_view, create_post
from django.views.generic import TemplateView
# instancia del enrutador y registra las vistas
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    # Definición de patrones de URL
    path('admin/', admin.site.urls),
    path('usuarios/', UsuarioViewSet.as_view({'get': 'list', 'post': 'create'}), name='usuarios'),
    path('comentarios/', ComentarioViewSet.as_view({'get': 'list'}), name='comentarios'),
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='posts'),
    path('login/', login_view, name='login'),
    path('', TemplateView.as_view(template_name='post/home.html'), name='home'),  # URL raíz para la template home.html
    path('register/', register_view, name='register'),
    path('create-post/', create_post, name='create_post'),
    # Resto de las URLs
]

