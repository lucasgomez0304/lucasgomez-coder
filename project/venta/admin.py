from django.contrib import admin

from . import models

class VentaAdmin(admin.ModelAdmin):
    list_display = (
        "vendedor",
        "publicacion",
        "precio",
        "fecha_venta",
    )
    list_display_links = ("publicacion",)
    search_fields = ("publicacion.nombre", "vendedor")
    list_filter = ("vendedor",)
    date_hierarchy = "fecha_venta"


admin.site.register(models.Vendedor)
admin.site.register(models.Venta, VentaAdmin)