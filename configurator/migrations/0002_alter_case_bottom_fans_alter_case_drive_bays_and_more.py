# Generated by Django 5.0.1 on 2024-12-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='bottom_fans',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Вентиляторы на нижней панели'),
        ),
        migrations.AlterField(
            model_name='case',
            name='drive_bays',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name="Отсеки для накопителей (например, 2x3.5', 2x2.5')"),
        ),
        migrations.AlterField(
            model_name='case',
            name='top_fans',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Вентиляторы на верхней панели'),
        ),
        migrations.AlterField(
            model_name='case',
            name='warranty',
            field=models.IntegerField(blank=True, null=True, verbose_name='Гарантия (мес.)'),
        ),
        migrations.AlterField(
            model_name='case',
            name='weight_kg',
            field=models.FloatField(blank=True, null=True, verbose_name='Вес'),
        ),
    ]
