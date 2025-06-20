# Generated by Django 5.2.1 on 2025-06-17 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_servicio_destacado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='destacado',
            field=models.BooleanField(default=False, help_text='Marcar para que este servicio aparezca en la sección de destacados.', verbose_name='Servicio Destacado'),
        ),
    ]
