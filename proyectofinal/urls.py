from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from blog.views import ComentarioViewSet, PostViewSet, create_post,categoria_noticias_view,categoria_reconciliacion_view,categoria_memorias_view,post_detail
from blog.views import (
    ChangePasswordUpdateAPIView,
    LoginView,
    RegisterView,
    UserModelViewSet,
    UserDestoyAPIView,
    UserUpdateAPIView,
)
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'comentarios', ComentarioViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    # Definición de patrones de URL
    #admin
    path('admin/', admin.site.urls),
    #post
    path('api/', include(router.urls)),
    path('comentarios/', ComentarioViewSet.as_view({'get': 'list'}), name='comentarios'),
    path('create-post/', create_post, name='create_post'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('api/posts/', PostViewSet.as_view({'get': 'list'}), name='post-list'),
    #login
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    #path("logout/", LogoutView.as_view(), name="knox_logout"),
    path(
        "update-password/",
        ChangePasswordUpdateAPIView.as_view(),
        name="update_password_api",
    ),
    path("user/<int:pk>/", UserDestoyAPIView.as_view(), name="user_delete"),
    path("update-user/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update"),
    #home
    path('', TemplateView.as_view(template_name='post/home.html'), name='home'),  # URL raíz para la template home.html
    #category
    path('categoria/posts/<str:noticias>/', categoria_noticias_view, name='categoria_noticias'),
    path('categoria/posts/<str:memoria>/', categoria_memorias_view, name='categoria_memorias'),
    path('categoria/posts/<str:reconciliacion>', categoria_reconciliacion_view, name='categoria_reconciliacion'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
