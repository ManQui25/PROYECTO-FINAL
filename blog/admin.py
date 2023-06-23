from django.contrib import admin
from .models import User, Noticia, Reconciliacion, Memoria, Comentario
# Register your models here.


admin.site.register(User)
admin.site.register(Noticia)
admin.site.register(Reconciliacion)
admin.site.register(Memoria)
admin.site.register(Comentario)
