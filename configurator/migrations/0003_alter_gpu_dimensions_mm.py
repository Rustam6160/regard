# Generated by Django 5.0.1 on 2024-12-17 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0002_gpu_dimensions_mm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpu',
            name='dimensions_mm',
            field=models.IntegerField(default=199, verbose_name='Шырина (длина) мм'),
        ),
    ]