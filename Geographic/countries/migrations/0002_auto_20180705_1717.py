# Generated by Django 2.0.7 on 2018-07-05 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(choices=[('colombia', 'CO'), ('Peru', 'PE'), ('Argentina', 'ARG'), ('Usa', 'USA')], max_length=20, verbose_name='Codigo'),
        ),
    ]
