from django.shortcuts import render,redirect
from .models import Platillo

# Create your views here.

def inicio_vista(request):
    losplatillos = Platillo.objects.all()

    return render(request,"gestionarPlatillo.html",{"misplatillos":losplatillos})



def registrarPlatillo(request):
    id_platillo = request.POST["txtidplatillo"]
    nombre_platillo = request.POST["txtdnombresplatillo"]
    descripcion = request.POST["txtdescripcion"]
    ingredientes = request.POST["txtingredientes"]
    precio = request.POST["txtprecio"]
    calorias = request.POST["txtcalorias"]
    tipo = request.POST["txttipo"]
    cantidad = request.POST["txtcantidad"]

    guardarplatillo = Platillo.objects.create(id_platillo=id_platillo, nombre_platillo=nombre_platillo, descripcion=descripcion,
                                              ingredientes=ingredientes, precio=precio, calorias=calorias, tipo=tipo, cantidad=cantidad)

    return redirect("/")

def seleccionarPlatillo(request, id_platillo):
    platillo = Platillo.objects.get(id_platillo = id_platillo)

    return render(request,"editarPlatillo.html",{"misplatillos":platillo})


def editarPlatillo(request):
    id_platillo = request.POST["txtidplatillo"]
    nombre_platillo = request.POST["txtnombresplatillo"]
    descripcion = request.POST["txtdescripcion"]
    ingredientes = request.POST["txtingredientes"]
    precio = request.POST["txtprecio"]
    calorias = request.POST["txtcalorias"]
    tipo = request.POST["txttipo"]
    cantidad = request.POST["txtcantidad"]

    sucursal = Platillo.objects.get(id_sucursal = id_sucursal)
    sucursal.nombre_sucursal = nombre_sucursal
    sucursal.ubicacion = ubicacion
    sucursal.horarios = horarios
    sucursal.celular = celular
    sucursal.encargado = encargado
    sucursal.email = email

    sucursal.save()

    return redirect("/")


def borrarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal = id_sucursal)
    sucursal.delete()

    return redirect("/")