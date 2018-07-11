from django.db import models

# Create your models here.

class EjercicioGuia(models.Model):
    """Model definition for EjercicioGuia."""
    # todo: Define fields here
    name = models.CharField(verbose_name="Nombre", max_length=250)
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to='core')
    url = models.URLField(verbose_name="Url", max_length=200)
    created = models.DateTimeField(verbose_name="Fecha de creacion", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de actualizacion", auto_now=True)

    class Meta:
        """Meta definition for EjercicioGuia."""

        verbose_name = 'EjercicioGuia'
        verbose_name_plural = 'Ejercicios Guias'
        ordering = ['-updated']

    def __str__(self):
        """Unicode representation of EjercicioGuia."""
        return self.name
