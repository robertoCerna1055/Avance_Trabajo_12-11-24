# Generated by Django 5.1.1 on 2024-11-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id_platillo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre_platillo', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=100)),
                ('ingredientes', models.CharField(max_length=100)),
                ('precio', models.IntegerField(max_length=10)),
                ('calorias', models.IntegerField(max_length=10)),
                ('tipo', models.CharField(max_length=45)),
                ('cantidad', models.IntegerField(max_length=10)),
            ],
        ),
    ]
