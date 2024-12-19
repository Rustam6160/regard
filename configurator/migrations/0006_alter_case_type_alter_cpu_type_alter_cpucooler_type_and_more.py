# Generated by Django 5.0.1 on 2024-12-19 16:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0005_alter_case_image_alter_cpu_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='type',
            field=models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'CPUCooler')], max_length=40),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='type',
            field=models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'CPUCooler')], max_length=40),
        ),
        migrations.AlterField(
            model_name='cpucooler',
            name='type',
            field=models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'CPUCooler')], max_length=40),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='type',
            field=models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'CPUCooler')], max_length=40),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='type',
            field=models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'CPUCooler')], max_length=40),
        ),
        migrations.AlterField(
            model_name='os',
            name='type',
            field=models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'CPUCooler')], max_length=40),
        ),
        migrations.AlterField(
            model_name='psu',
            name='type',
            field=models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'CPUCooler')], max_length=40),
        ),
        migrations.AlterField(
            model_name='ram',
            name='type',
            field=models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'CPUCooler')], max_length=40),
        ),
        migrations.AlterField(
            model_name='storage',
            name='type',
            field=models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'CPUCooler')], max_length=40),
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.case')),
                ('cpu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.cpu')),
                ('gpu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.gpu')),
                ('motherboard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.motherboard')),
                ('os', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.os')),
                ('psu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.psu')),
                ('ram', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.ram')),
                ('spucooler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.cpucooler')),
                ('storage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.storage')),
            ],
        ),
    ]
