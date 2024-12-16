# from django.shortcuts import render <-- esta libreria no la usamos por ahora
from rest_framework import viewsets
from .serializer import *
from .models import *
# Create your views here.
class ProgrammerViewSet(viewsets.ModelViewSet):
    # acá creamos una consulta o QUERY a nuestra tabla, trayendo todos los campos como un objeto.
    queryset = programmer.objects.all()
    # Agregamos la clase ProgrammerSerializer que ya tiene el modelo serializado para mostrar
    serializer_class = ProgrammerSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer