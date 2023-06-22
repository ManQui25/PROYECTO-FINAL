from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    # Añadir cualquier atributo adicional si es necesario
    edad = models.PositiveIntegerField(null=True, blank=True)
    # Agregar campos groups y user_permissions con nombres relacionados personalizados
    groups = models.ManyToManyField(
        Group,
        verbose_name='Grupos',
        related_name='usuarios_personalizado'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='Permisos de usuario',
        related_name='usuarios_personalizado'
    )

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

    def __str__(self):
        return self.title

class Noticia(Post):
    # Añadir cualquier atributo adicional si es necesario
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

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
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
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
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    departamento = models.CharField(max_length=255, choices=DEPARTAMENTOS, default='amazonas')

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.user.username} en {self.post.title}"

