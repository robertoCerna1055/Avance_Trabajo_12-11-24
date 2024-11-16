from django.urls import path
from Platillos_app import views 

urlpatterns = [
    path("",views.inicio_vista,name="inicio_vista"),
    path("registrarPlatillo/",views.registrarPlatillo,name="registrarPlatillo"),
    path("seleccionarPlatillo/<id_platillo>",views.seleccionarPlatillo,name="seleccionarPlatillo"),
    path("editarPlatillo/",views.editarPlatillo,name="editarPlatillo"),
    path("borrarPlatillo/<id_platillo>",views.borrarPlatillo,name="borrarPlatillo"),
]