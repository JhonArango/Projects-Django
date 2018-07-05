# Generated by Django 2.0.7 on 2018-07-05 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
            ],
            options={
                'verbose_name': 'Continente',
                'verbose_name_plural': 'Continente',
                'ordering': ['name'],
            },
        ),
    ]
