from django.db import models

class Pais(models.Model):
    pais = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.pais
    
    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"


class Ciudad(models.Model):
    ciudad = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.ciudad
    
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
    

class Publicacion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=600)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
    

