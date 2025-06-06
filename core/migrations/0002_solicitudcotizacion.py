# Generated by Django 5.2.1 on 2025-05-22 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudCotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=150)),
                ('email_cliente', models.EmailField(max_length=254)),
                ('telefono_cliente', models.CharField(blank=True, max_length=20, null=True)),
                ('descripcion_evento', models.TextField(help_text='Describe brevemente el servicio o evento que te interesa')),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('atendida', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Solicitud de Cotización',
                'verbose_name_plural': 'Solicitudes de Cotización',
                'ordering': ['-fecha_solicitud'],
            },
        ),
    ]
