from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here
    categories = models.ManyToManyField('products.ProduCategory')
    title = models.CharField(verbose_name="Producto", max_length=255)
    description = models.CharField(verbose_name="Descripcion", max_length=250)
    price = models.IntegerField(verbose_name="Precio")
    slug = models.SlugField(verbose_name="Slug")
    created = models.DateTimeField(verbose_name="Fecha de creacion",auto_now_add=True)
    updated = models.DateField(verbose_name="Fecha de actualizacion",auto_now=True)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        """Meta definition for Product."""
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['title']

    def __str__(self):
        """Unicode representation of Product."""
        return self.title

class ProducImage(models.Model):
    """Model definition for ProducImage."""
    # TODO: Define fields here
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name="Imagen",upload_to='products')

    class Meta:
        """Meta definition for ProducImage."""
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

    def __str__(self):
        """Unicode representation of ProducImage."""
        return self.image.url


class ProduCategory(models.Model):
    """Model definition for ProduCategory."""

    # TODO: Define fields here
    name = models.CharField(verbose_name="Nombre", max_length=255)
    slug = models.SlugField(verbose_name="Slug")
    created = models.DateTimeField(verbose_name="Fecha de creacion",auto_now_add=True)
    updated = models.DateField(verbose_name="Fecha de actualizacion",auto_now=True)

    class Meta:
        """Meta definition for ProduCategory."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of ProduCategory."""
        return self.name
