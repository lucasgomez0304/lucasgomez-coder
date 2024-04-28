from django.db import models

class Pais(models.Model):
    pais = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.pais


class Ciudad(models.Model):
    ciudad = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.ciudad
    

class Publicacion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=600)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.nombre
    

