# Generated by Django 5.0.6 on 2024-06-16 01:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0003_auto_foto_alter_auto_cantidad_alter_auto_color"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Comprador",
            new_name="Cliente",
        ),
        migrations.RenameField(
            model_name="venta",
            old_name="comprador",
            new_name="cliente",
        ),
    ]
