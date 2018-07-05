from django.db import models

# Create your models here.
class Continent(models.Model):
    name = models.CharField(max_length=100,verbose_name='Nombre')
    color = models.CharField(max_length=50,verbose_name='Color')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Continente'
        verbose_name_plural = 'Continente'
        ordering = ['name']