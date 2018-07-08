# Generated by Django 2.0.6 on 2018-07-08 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producategory',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='producimage',
            options={'verbose_name': 'Imagen', 'verbose_name_plural': 'Imagenes'},
        ),
        migrations.AddField(
            model_name='producimage',
            name='categories',
            field=models.ManyToManyField(to='products.ProduCategory'),
        ),
        migrations.AlterField(
            model_name='producimage',
            name='image',
            field=models.ImageField(upload_to='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateField(auto_now=True, verbose_name='Fecha de actualizacion'),
        ),
    ]