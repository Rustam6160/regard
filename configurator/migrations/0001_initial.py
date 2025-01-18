# Generated by Django 5.0.1 on 2025-01-16 16:50

import configurator.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('сpucooler', 'CPUCooler')], max_length=40)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название операционной системы')),
                ('line', models.CharField(default='Windows 11', max_length=50, verbose_name='Линейка')),
                ('release', models.CharField(default='Professional', max_length=50, verbose_name='Выпуск')),
                ('bit_version', models.CharField(default='64 bit', max_length=20, verbose_name='Битность')),
                ('supply_type', models.CharField(default='OEM (только в комплекте с ПК)', max_length=50, verbose_name='Тип поставки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/os/', verbose_name='Фото операционной системы')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='os', to='configurator.product')),
            ],
            bases=(configurator.models.AutoCreateProductMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название материнской платы')),
                ('socket', models.CharField(default='LGA 1700', max_length=50, verbose_name='Сокет')),
                ('chipset', models.CharField(default='Intel B760', max_length=50, verbose_name='Чипсет')),
                ('ram_type', models.CharField(default='DDR4', max_length=50, verbose_name='Тип ОЗУ')),
                ('max_ram', models.IntegerField(default=128, verbose_name='Максимальный объем ОЗУ, ГБ')),
                ('ram_slots', models.IntegerField(default=4, verbose_name='Количество слотов ОЗУ')),
                ('form_factor', models.CharField(default='ATX', max_length=50, verbose_name='Форм-фактор')),
                ('m2_slots', models.IntegerField(blank=True, null=True, verbose_name='Количество слотов M.2')),
                ('sata_ports', models.IntegerField(blank=True, null=True, verbose_name='Количество SATA портов')),
                ('pcie_version', models.CharField(default='PCI Express 4.0', max_length=50, verbose_name='Версия PCIe')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/motherboards/', verbose_name='Фото материнской платы')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='motherboard', to='configurator.product')),
            ],
            bases=(configurator.models.AutoCreateProductMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название видеокарты')),
                ('interface', models.CharField(default='PCI Express 4.0', max_length=50, verbose_name='Интерфейс')),
                ('manufacturer_gpu', models.CharField(default='unknown', max_length=100, verbose_name='Производитель видеопроцессора')),
                ('series', models.CharField(default='unknown', max_length=50, verbose_name='Серия')),
                ('memory_size', models.IntegerField(default=8000, verbose_name='Объём памяти мб')),
                ('memory_type', models.CharField(default='GDDR6', max_length=50, verbose_name='Тип памяти')),
                ('memory_bus', models.IntegerField(default=128, verbose_name='Шина памяти (разрядность)')),
                ('dimensions_mm', models.IntegerField(default=199, verbose_name='Шырина (длина) мм')),
                ('gpu_base_clock', models.IntegerField(default=1830, verbose_name='Частота графического процессора')),
                ('gpu_boost_clock', models.IntegerField(default=2505, verbose_name='Частота графического процессора (Boost)')),
                ('cuda_cores', models.IntegerField(default=3072, verbose_name='Число универсальных процессоров')),
                ('recommended_psu_power', models.IntegerField(default=550, verbose_name='Рекомендуемая мощность блока питания')),
                ('tgp', models.IntegerField(default=115, verbose_name='TGP')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/gpu/', verbose_name='Фото видеокарты')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gpu', to='configurator.product')),
            ],
            bases=(configurator.models.AutoCreateProductMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CPUCooler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название кулера')),
                ('socket_compatibility', models.CharField(default='LGA 115x/1200, LGA 1700, 1851, AM4, AM5', max_length=255, verbose_name='Совместимые сокеты')),
                ('cooler_type', models.CharField(default='активная', max_length=50, verbose_name='Тип системы охлаждения')),
                ('max_power_dissipation', models.IntegerField(default=220, verbose_name='Максимальная рассеиваемая мощность, Вт')),
                ('fan_count', models.IntegerField(default=1, verbose_name='Количество вентиляторов')),
                ('fan_size_mm', models.CharField(default='120x120 мм', max_length=50, verbose_name='Размеры вентилятора, мм')),
                ('fan_speed_rpm', models.CharField(default='600-1500 об/мин', max_length=50, verbose_name='Скорость вращения вентилятора')),
                ('fan_noise_level_db', models.FloatField(default=28.9, verbose_name='Уровень шума вентилятора, дБ')),
                ('airflow_cfm', models.IntegerField(default=70, verbose_name='Воздушный поток, CFM')),
                ('speed_control', models.CharField(default='PWM', max_length=50, verbose_name='Регулятор оборотов')),
                ('lighting', models.BooleanField(default=False, verbose_name='Подсветка')),
                ('height_mm', models.IntegerField(default=151, verbose_name='Высота кулера, мм')),
                ('weight_kg', models.FloatField(default=0.65, verbose_name='Вес, кг')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/coolers/', verbose_name='Фото кулера')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cpucooler', to='configurator.product')),
            ],
            bases=(configurator.models.AutoCreateProductMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название процессора')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/CPU/', verbose_name='Фото CPU')),
                ('manufacturer', models.CharField(default='Intel', max_length=100, verbose_name='Производитель')),
                ('socket', models.CharField(default='LGA 1700', max_length=50, verbose_name='Socket')),
                ('architecture', models.CharField(blank=True, max_length=50, null=True, verbose_name='Архитектура')),
                ('cores', models.IntegerField(default=4, verbose_name='Количество ядер')),
                ('threads', models.IntegerField(blank=True, null=True, verbose_name='Количество потоков')),
                ('base_clock', models.FloatField(blank=True, null=True, verbose_name='Тактовая частота')),
                ('turbo_clock', models.FloatField(blank=True, null=True, verbose_name='Частота процессора в режиме Turbo')),
                ('tdp', models.IntegerField(blank=True, null=True, verbose_name='Типичное тепловыделение')),
                ('release_date', models.CharField(blank=True, max_length=50, null=True, verbose_name='Дата релиза')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cpu', to='configurator.product')),
            ],
            bases=(configurator.models.AutoCreateProductMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название корпуса')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/cases/', verbose_name='Фото корпуса')),
                ('max_gpu_length_mm', models.IntegerField(default=315, verbose_name='Максимальная длина видеокарты, мм')),
                ('max_cpu_cooler_height_mm', models.IntegerField(default=163, verbose_name='Максимальная высота кулера, мм')),
                ('form_factor_support', models.CharField(default='ATX, mATX, Mini-ITX', max_length=100, verbose_name='Поддерживаемые форм-факторы материнских плат')),
                ('psu_type', models.CharField(default='без БП', max_length=50, verbose_name='Тип блока питания (например, ATX, SFX)')),
                ('drive_bays', models.CharField(blank=True, max_length=100, null=True, verbose_name="Отсеки для накопителей (например, 2x3.5', 2x2.5')")),
                ('fan_slots', models.BooleanField(default=True, verbose_name='Места для вентиляторов')),
                ('bottom_fans', models.CharField(blank=True, max_length=50, null=True, verbose_name='Вентиляторы на нижней панели')),
                ('top_fans', models.CharField(blank=True, max_length=50, null=True, verbose_name='Вентиляторы на верхней панели')),
                ('rgb_lighting', models.BooleanField(default=True, verbose_name='Подсветка корпуса')),
                ('liquid_cooling_support', models.BooleanField(default=True, verbose_name='Возможность установки СЖО')),
                ('dimensions', models.CharField(default='204 x 446 x 396 мм', max_length=50, verbose_name='Размеры (ШхВхГ)')),
                ('weight_kg', models.FloatField(blank=True, null=True, verbose_name='Вес')),
                ('warranty', models.IntegerField(blank=True, null=True, verbose_name='Гарантия (мес.)')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='case', to='configurator.product')),
            ],
            bases=(configurator.models.AutoCreateProductMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PSU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название блока питания')),
                ('power', models.IntegerField(default=750, verbose_name='Мощность, Вт')),
                ('efficiency_rating', models.CharField(default='Standard', max_length=50, verbose_name='Коэффициент эффективности')),
                ('modularity', models.CharField(blank=True, choices=[('Modular', 'Модульный'), ('Non-Modular', 'Немодульный'), ('Semi-Modular', 'Полумодульный')], max_length=50, null=True, verbose_name='Тип кабелей')),
                ('pcie_connectors', models.IntegerField(default=4, verbose_name='Количество разъемов PCIe')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/psu/', verbose_name='Фото блока питания')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='psu', to='configurator.product')),
            ],
            bases=(configurator.models.AutoCreateProductMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название ОЗУ')),
                ('form_factor', models.CharField(default='DIMM', max_length=50, verbose_name='Форм-фактор')),
                ('memory_type', models.CharField(default='DDR4', max_length=50, verbose_name='Тип ОЗУ')),
                ('capacity', models.IntegerField(default=8, verbose_name='Объем ОЗУ, ГБ')),
                ('module_capacity', models.IntegerField(default=16, verbose_name='Объем одного модуля, ГБ')),
                ('kit_modules', models.IntegerField(default=2, verbose_name='Количество модулей в комплекте')),
                ('frequency', models.IntegerField(default=6000, verbose_name='Частота, МГц')),
                ('cas_latency', models.IntegerField(default=40, verbose_name='CAS Latency (CL)')),
                ('voltage', models.FloatField(default=1.35, verbose_name='Напряжение питания, В')),
                ('xmp_support', models.BooleanField(default=True, verbose_name='Поддержка XMP')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/ram/', verbose_name='Фото ОЗУ')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ram', to='configurator.product')),
            ],
            bases=(configurator.models.AutoCreateProductMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название накопителя')),
                ('storage_type', models.CharField(choices=[('HDD', 'HDD'), ('SSD', 'SSD'), ('NVMe', 'NVMe')], default='HDD', max_length=50, verbose_name='Тип накопителя')),
                ('capacity_gb', models.IntegerField(default=8000, verbose_name='Емкость, ГБ')),
                ('rpm', models.IntegerField(blank=True, null=True, verbose_name='Скорость вращения шпинделя, об/мин')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/storage/', verbose_name='Фото накопителя')),
                ('form_factor', models.CharField(default='3.5"', max_length=50, verbose_name='Форм-фактор')),
                ('interface', models.CharField(default='SATA-III', max_length=50, verbose_name='Интерфейс подключения')),
                ('warranty', models.IntegerField(default=12, verbose_name='Гарантия (мес.)')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='storage', to='configurator.product')),
            ],
            bases=(configurator.models.AutoCreateProductMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.case')),
                ('cpu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.cpu')),
                ('cpucooler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.cpucooler')),
                ('gpu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.gpu')),
                ('motherboard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.motherboard')),
                ('os', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.os')),
                ('psu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.psu')),
                ('ram', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.ram')),
                ('storage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.storage')),
            ],
        ),
    ]
