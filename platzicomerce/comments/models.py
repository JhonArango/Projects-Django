from django.db import models
from django.conf import settings

# Create your models here.
class Comment(models.Model):
    """Model definition for Comment."""
    # TODO: Define fields here
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='comments',verbose_name="Autor")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE,related_name='comments')
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(verbose_name="Fecha de creacion",auto_now_add=True)
    updated = models.DateField(verbose_name="Fecha de actualizacion",auto_now=True)

    class Meta:
        """Meta definition for Comment."""
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        """Unicode representation of Comment."""
        return self.content[:20]
