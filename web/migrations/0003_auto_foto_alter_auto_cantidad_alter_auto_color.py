# Generated by Django 5.0.6 on 2024-06-15 18:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0002_remove_auto_vendedor_remove_auto_vendido_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="auto",
            name="foto",
            field=models.ImageField(blank=True, null=True, upload_to="autos/"),
        ),
        migrations.AlterField(
            model_name="auto",
            name="cantidad",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="auto",
            name="color",
            field=models.CharField(max_length=100),
        ),
    ]