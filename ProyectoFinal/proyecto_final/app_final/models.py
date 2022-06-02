from django.db import models
from django.forms import IntegerField

# Create your models here.


class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=40, unique=True)
    email_usuario = models.EmailField(max_length=40)
    fecha_registro = models.DateField(auto_now_add= True)
    #tipo_usuario = IntegerField() #0 == usuario normal, 1 == usuario con privilegios administrativos
    #pass_usuario = models.CharField(max_lenght=40) 

class Juego(models.Model):
    nombre_juego = models.CharField(max_length=40, unique=True)
    genero_juego = models.CharField(max_length=40)
    desarrollador = models.CharField(max_length=40)

class Review(models.Model):
    nombre_autor = models.CharField(max_length=40)
    fecha_review = models.DateField(auto_now_add=True)
    titulo_review = models.CharField(max_length=40)
    contenido_review = models.CharField(max_length=200)
    puntaje_review = models.IntegerField()
    juego_review = models.CharField(max_length=40)




