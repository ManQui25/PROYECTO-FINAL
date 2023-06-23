from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for hotelapp."""

    email = models.EmailField(_("email address"), blank=True, unique=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    phone_number = models.CharField(_("Phone number"), max_length=30)
    groups = models.ManyToManyField(
        Group,
        verbose_name='Grupos',
        related_name='users_custom',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='Permisos de usuario',
        related_name='users_custom',
    )      
    def get_absolute_url(self):
        """Get url for user's detail view.
        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"username": self.username})

    # cookiecutter

    def __str__(self):
        return self.username

class Post(models.Model):
    CATEGORIAS = (
        ('noticias', 'Noticias'),
        ('memorias', 'Memorias'),
        ('reconciliacion', 'Reconciliación'),
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=255, choices=CATEGORIAS)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/',null=True, blank=True)

    def __str__(self):
        return self.title

class Noticia(Post):
    # Añadir cualquier atributo adicional si es necesario
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Memoria(Post):
    DEPARTAMENTOS = (
        ('amazonas', 'Amazonas'),
        ('antioquia', 'Antioquia'),
        ('arauca', 'Arauca'),
        ('atlantico', 'Atlántico'),
        ('bogota', 'Bogotá'),
        ('bolivar', 'Bolívar'),
        ('boyaca', 'Boyacá'),
        ('caldas', 'Caldas'),
        ('caqueta', 'Caquetá'),
        ('cauca', 'Cauca'),
        ('cesar', 'Cesar'),
        ('choco', 'Chocó'),
        ('cordoba', 'Córdoba'),
        ('cundinamarca', 'Cundinamarca'),
        ('guaviare', 'Guaviare'),
        ('huila', 'Huila'),
        ('guajira', 'Guajira'),
        ('magdalena', 'Magdalena'),
        ('meta', 'Meta'),
        ('nariño', 'Nariño'),
        ('norte de santander', 'Norte de Santander'),
        ('putumayo', 'Putumayo'),
        ('quindio', 'Quindio'),
        ('risaralda', 'Risaralda'),
        ('san andres y providencia', 'San Andrés y Providencia'),
        ('santander', 'Santander'),
        ('sucre', 'Sucre'),
        ('tolima', 'Tolima'),
        ('valle del cauca', 'Valle del Cauca'),
        ('vaupes', 'Vaupés'),
        ('vichada', 'Vichada'),
    )
    # Añadir cualquier atributo adicional si es necesario
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    departamento = models.CharField(max_length=255, choices=DEPARTAMENTOS, default='amazonas')

class Reconciliacion(Post):
    DEPARTAMENTOS = (
        ('amazonas', 'Amazonas'),
        ('antioquia', 'Antioquia'),
        ('arauca', 'Arauca'),
        ('atlantico', 'Atlántico'),
        ('bogota', 'Bogotá'),
        ('bolivar', 'Bolívar'),
        ('boyaca', 'Boyacá'),
        ('caldas', 'Caldas'),
        ('caqueta', 'Caquetá'),
        ('cauca', 'Cauca'),
        ('cesar', 'Cesar'),
        ('choco', 'Chocó'),
        ('cordoba', 'Córdoba'),
        ('cundinamarca', 'Cundinamarca'),
        ('guaviare', 'Guaviare'),
        ('huila', 'Huila'),
        ('guajira', 'Guajira'),
        ('magdalena', 'Magdalena'),
        ('meta', 'Meta'),
        ('nariño', 'Nariño'),
        ('norte de santander', 'Norte de Santander'),
        ('putumayo', 'Putumayo'),
        ('quindio', 'Quindio'),
        ('risaralda', 'Risaralda'),
        ('san andres y providencia', 'San Andrés y Providencia'),
        ('santander', 'Santander'),
        ('sucre', 'Sucre'),
        ('tolima', 'Tolima'),
        ('valle del cauca', 'Valle del Cauca'),
        ('vaupes', 'Vaupés'),
        ('vichada', 'Vichada'),
    )
    # Añade cualquier atributo adicional si es necesario
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    departamento = models.CharField(max_length=255, choices=DEPARTAMENTOS, default='amazonas')

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.user.username} en {self.post.title}"

