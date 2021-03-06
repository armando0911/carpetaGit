# Generated by Django 4.0.5 on 2022-06-30 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_alter_cursos_options_alter_cursos_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='duracion_hrs',
            field=models.PositiveIntegerField(verbose_name='Horas de duración'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nombre',
            field=models.TextField(max_length=40, verbose_name='Nombre del curso'),
        ),
    ]
