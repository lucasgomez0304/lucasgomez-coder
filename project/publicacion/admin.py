from django.contrib import admin

from . import models

admin.site.register(models.Pais)
admin.site.register(models.Ciudad)
admin.site.register(models.Publicacion)
