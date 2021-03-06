# Generated by Django 4.0.5 on 2022-06-27 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=15)),
                ('descripcion', models.TextField()),
                ('duracion_hrs', models.PositiveIntegerField()),
                ('instructor', models.TextField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
