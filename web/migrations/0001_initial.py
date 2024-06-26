# Generated by Django 5.0.6 on 2024-06-15 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comprador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("correo_electronico", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Vendedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("correo_electronico", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Auto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("marca", models.CharField(max_length=100)),
                ("modelo", models.CharField(max_length=100)),
                ("año", models.IntegerField()),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("vendido", models.BooleanField(default=False)),
                (
                    "vendedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.vendedor"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Venta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_venta", models.DateTimeField(auto_now_add=True)),
                (
                    "auto",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="web.auto"
                    ),
                ),
                (
                    "comprador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.comprador"
                    ),
                ),
            ],
        ),
    ]
