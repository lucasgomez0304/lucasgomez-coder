from django.urls import path

app_name = "publicacion"

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("crear/", views.publicacion_crear, name="publicacion_crear"),
    path("ciudades/", views.ciudades, name="ciudades"),
]
