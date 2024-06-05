from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    grado = models.CharField(max_length=50)

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class ActividadExtracurricular(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()