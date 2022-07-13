# Generated by Django 4.0.5 on 2022-07-06 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_actividad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id_registro', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('nombre_u', models.TextField(verbose_name='Nombre')),
                ('apellido_p', models.TextField(verbose_name='Apellido paterno')),
                ('apellido_m', models.TextField(verbose_name='Apellido materno')),
                ('correo', models.CharField(max_length=70, verbose_name='Correo')),
                ('mensaje_u', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
                ('curso_u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos', verbose_name='Curso')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
                'ordering': ['-created'],
            },
        ),
    ]