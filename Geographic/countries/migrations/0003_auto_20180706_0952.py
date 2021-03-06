# Generated by Django 2.0.7 on 2018-07-06 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0001_initial'),
        ('countries', '0002_auto_20180705_1717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Pais', 'verbose_name_plural': 'Paises'},
        ),
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='continents.Continent'),
            preserve_default=False,
        ),
    ]
