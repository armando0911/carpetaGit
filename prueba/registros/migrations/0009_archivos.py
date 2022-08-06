# Generated by Django 4.0.5 on 2022-08-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0008_alumnos_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('idar', models.AutoField(primary_key=True, serialize=False, verbose_name='id archivos')),
                ('titulo', models.CharField(max_length=100, verbose_name='titulo')),
                ('descripcion', models.CharField(max_length=100, verbose_name='descripcion')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archivos')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Archivo',
                'verbose_name_plural': 'Archivos',
                'ordering': ['-created'],
            },
        ),
    ]
