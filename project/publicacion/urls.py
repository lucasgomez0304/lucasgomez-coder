from django.urls import path

app_name = "publicacion"

from . import views

urlpatterns = [
    path("", views.home, name="home")
]
