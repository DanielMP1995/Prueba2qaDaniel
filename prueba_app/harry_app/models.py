from django.db import models

class Personaje(models.Model):
    nombre = models.CharField(max_length=150)
    apodo = models.CharField(max_length=150, blank=True)
    casa = models.CharField(max_length=100)
    actor = models.CharField(max_length=150)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre