from django.db import models
from countries.models import Country

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=200,verbose_name="Primer Nombre")
    nacionalidad = models.ManyToManyField(Country)
    father = models.OneToOneField('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'