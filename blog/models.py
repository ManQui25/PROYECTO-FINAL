from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # Añadir cualquier atributo adicional si es necesario
    edad = models.PositiveIntegerField(null=True, blank=True)

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
    # Añadir cualquier atributo adicional si es necesario
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    ubicacion = models.CharField(max_length=255)

class Reconciliacion(Post):
    # Añade cualquier atributo adicional si es necesario
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_reconciliacion = models.DateField()

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.user.username} en {self.post.title}"

