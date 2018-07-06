from django.db import models

# Create your models here.
class Country(models.Model):
    CODES_CHOISES=(
        ('colombia','CO'),
        ('Peru','PE'),
        ('Argentina','ARG'),
        ('Usa','USA'),

    )
    name = models.CharField(max_length=100,verbose_name='Nombre')
    code = models.CharField(max_length=20,verbose_name='Codigo',choices=CODES_CHOISES)
    continent = models.ForeignKey('continents.Continent', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'