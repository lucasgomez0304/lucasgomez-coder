from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from django.utils import timezone


class Vendedor(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, related_name="vendedor"
    )
    celular = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self) -> str:
        return self.usuario.username


class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    publicacion = models.ForeignKey("publicacion.Publicacion", on_delete=models.DO_NOTHING)
    precio = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ("-fecha_venta",)

    def save(self, *args, **kwargs):
        self.precio = self.publicacion.precio 
        super().save(*args, **kwargs)
