from django.db import models


class Estudiantes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    comision = models.CharField(max_length=100)

