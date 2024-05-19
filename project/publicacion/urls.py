from django.urls import path

app_name = "publicacion"

from . import views

# PUBLICACION
urlpatterns = [
    path("", views.home, name="home"),

    path("list/", views.PublicacionList.as_view(), name="publicacion_list"),

    path("create/", views.PublicacionCreate.as_view(), name="publicacion_create"),
    
    path("detail/<int:pk>", views.PublicacionDetail.as_view(), name="publicacion_detail"),
    
    path("update/<int:pk>", views.PublicacionUpdate.as_view(), name="publicacion_update"),
    
    path("delete/<int:pk>", views.PublicacionDelete.as_view(), name="publicacion_delete"),
]


#ciudades
urlpatterns += [
    path("ciudad/", views.CiudadList.as_view(), name="ciudad_list"),

    path("ciudad/create/", views.CiudadCreate.as_view(), name="ciudad_create"),

    path("ciudad/detail/<int:pk>", views.CiudadDetail.as_view(), name="ciudad_detail"),

    path("ciudad/update/<int:pk>", views.CiudadUpdate.as_view(), name="ciudad_update"),

    path("ciudad/delete/<int:pk>", views.CiudadDelete.as_view(), name="ciudad_delete"),
]


#paises
urlpatterns += [
    path("pais/list/", views.PaisList.as_view(), name="pais_list"),

    path("pais/create/", views.PaisCreate.as_view(), name="pais_create"),

    path("pais/detail/<int:pk>", views.PaisDetail.as_view(), name="pais_detail"),

    path("pais/update/<int:pk>", views.PaisUpdate.as_view(), name="pais_update"),

    path("pais/delete/<int:pk>", views.PaisDelete.as_view(), name="pais_delete"),
]