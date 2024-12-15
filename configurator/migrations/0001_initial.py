# Generated by Django 5.0.1 on 2024-12-15 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название корпуса')),
                ('type', models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'SPUCooler')], max_length=40)),
                ('form_factor_support', models.CharField(default='ATX, mATX, Mini-ITX', max_length=100, verbose_name='Поддерживаемые форм-факторы материнских плат')),
                ('max_gpu_length_mm', models.IntegerField(default=315, verbose_name='Максимальная длина видеокарты, мм')),
                ('max_cpu_cooler_height_mm', models.IntegerField(default=163, verbose_name='Максимальная высота кулера, мм')),
                ('drive_bays', models.CharField(default='2.5" - 2, 3.5" - 2', max_length=100, verbose_name="Отсеки для накопителей (например, 2x3.5', 2x2.5')")),
                ('psu_type', models.CharField(default='без БП', max_length=50, verbose_name='Тип блока питания (например, ATX, SFX)')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/cases/', verbose_name='Фото корпуса')),
                ('material', models.CharField(default='сталь', max_length=50, verbose_name='Материал корпуса')),
                ('side_window', models.BooleanField(default=True, verbose_name='Наличие окна на боковой стенке')),
                ('window_material', models.CharField(default='закалённое стекло', max_length=50, verbose_name='Материал окна')),
                ('expansion_slots', models.IntegerField(default=7, verbose_name='Количество слотов расширения')),
                ('hdd_mounting', models.CharField(default='поперечное', max_length=50, verbose_name='Размещение HDD')),
                ('max_psu_length_mm', models.IntegerField(default=180, verbose_name='Максимальная длина БП')),
                ('front_panel_ports', models.CharField(default='2 x USB 2.0, USB 3.0, аудио', max_length=100, verbose_name='Интерфейсы на лицевой панели')),
                ('fan_slots', models.BooleanField(default=True, verbose_name='Места для вентиляторов')),
                ('bottom_fans', models.CharField(default='2 x 120 мм', max_length=50, verbose_name='Вентиляторы на нижней панели')),
                ('top_fans', models.CharField(default='2 x 120 мм', max_length=50, verbose_name='Вентиляторы на верхней панели')),
                ('rear_fan', models.CharField(default='120 мм', max_length=50, verbose_name='Вентилятор на задней панели')),
                ('front_fans', models.CharField(default='3 x 140 мм', max_length=100, verbose_name='Вентиляторы на передней панели')),
                ('rgb_lighting', models.BooleanField(default=True, verbose_name='Подсветка корпуса')),
                ('rgb_type', models.CharField(default='FRGB (Fixed RGB)', max_length=50, verbose_name='Тип подсветки')),
                ('liquid_cooling_support', models.BooleanField(default=True, verbose_name='Возможность установки СЖО')),
                ('dust_filters', models.CharField(default='на верхней панели, на нижней панели', max_length=100, verbose_name='Пылевой фильтр')),
                ('additional_info', models.CharField(default='посадочные места передней панели совместимы с двумя вентиляторами 180 мм или тремя 120 мм', max_length=200, verbose_name='Дополнительная информация')),
                ('color_scheme', models.CharField(default='чёрный', max_length=50, verbose_name='Цвета оформления')),
                ('dimensions', models.CharField(default='204 x 446 x 396 мм', max_length=50, verbose_name='Размеры (ШхВхГ)')),
                ('weight_kg', models.FloatField(default=4.7, verbose_name='Вес')),
                ('warranty', models.IntegerField(default=12, verbose_name='Гарантия (мес.)')),
                ('manufacturer_website', models.URLField(default='www.zalman.com', verbose_name='Сайт производителя')),
            ],
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название процессора')),
                ('type', models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'SPUCooler')], max_length=40)),
                ('manufacturer', models.CharField(default='Intel', max_length=100, verbose_name='Производитель')),
                ('code', models.CharField(default='CM8071504555318/CM8071504650609', max_length=100, verbose_name='Код производителя')),
                ('line', models.CharField(default='Core i5', max_length=50, verbose_name='Линейка')),
                ('model', models.CharField(default='12400F', max_length=50, verbose_name='Модель')),
                ('socket', models.CharField(default='LGA 1700', max_length=50, verbose_name='Socket')),
                ('architecture', models.CharField(blank=True, max_length=50, null=True, verbose_name='Архитектура')),
                ('core', models.CharField(default='Golden Cove', max_length=50, verbose_name='Ядро')),
                ('cores', models.IntegerField(default=6, verbose_name='Количество ядер')),
                ('threads', models.IntegerField(blank=True, null=True, verbose_name='Количество потоков')),
                ('base_clock', models.FloatField(default=2500, verbose_name='Тактовая частота')),
                ('turbo_clock', models.FloatField(default=4400, verbose_name='Частота процессора в режиме Turbo')),
                ('bus_speed', models.CharField(blank=True, max_length=50, null=True, verbose_name='Частота шины')),
                ('multiplier', models.IntegerField(blank=True, null=True, verbose_name='Коэффициент умножения')),
                ('integrated_gpu', models.BooleanField(default=False, verbose_name='Интегрированное графическое ядро')),
                ('l1_cache', models.FloatField(blank=True, null=True, verbose_name='Объём кэша L1')),
                ('l2_cache', models.FloatField(blank=True, null=True, verbose_name='Объём кэша L2')),
                ('l3_cache', models.FloatField(blank=True, null=True, verbose_name='Объём кэша L3')),
                ('process_technology', models.CharField(blank=True, max_length=50, null=True, verbose_name='Технологический процесс')),
                ('max_temp', models.IntegerField(blank=True, null=True, verbose_name='Максимальная рабочая температура')),
                ('tdp', models.IntegerField(blank=True, null=True, verbose_name='Типичное тепловыделение')),
                ('technologies', models.TextField(blank=True, null=True, verbose_name='Технологии')),
                ('cooler_included', models.BooleanField(default=False, verbose_name='Кулер в комплекте')),
                ('release_date', models.CharField(blank=True, max_length=50, null=True, verbose_name='Дата релиза')),
                ('supply_type', models.CharField(default='OEM (без кулера)', max_length=50, verbose_name='Тип поставки')),
                ('warranty', models.IntegerField(default=12, verbose_name='Гарантия (мес.)')),
                ('website', models.URLField(default='www.intel.com', verbose_name='Сайт производителя')),
            ],
        ),
        migrations.CreateModel(
            name='CPUCooler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название кулера')),
                ('type', models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'SPUCooler')], max_length=40)),
                ('socket_compatibility', models.CharField(default='LGA 115x/1200, LGA 1700, 1851, AM4, AM5', max_length=255, verbose_name='Совместимые сокеты')),
                ('cooler_type', models.CharField(default='активная', max_length=50, verbose_name='Тип системы охлаждения')),
                ('max_power_dissipation', models.IntegerField(default=220, verbose_name='Максимальная рассеиваемая мощность, Вт')),
                ('heatpipes', models.BooleanField(default=True, verbose_name='Тепловые трубки')),
                ('radiator_material', models.CharField(default='алюминий', max_length=50, verbose_name='Материал радиатора')),
                ('base_material', models.CharField(default='алюминий/медь', max_length=50, verbose_name='Материал основания')),
                ('fan_count', models.IntegerField(default=1, verbose_name='Количество вентиляторов')),
                ('fan_size_mm', models.CharField(default='120x120 мм', max_length=50, verbose_name='Размеры вентилятора, мм')),
                ('fan_speed_rpm', models.CharField(default='600-1500 об/мин', max_length=50, verbose_name='Скорость вращения вентилятора')),
                ('fan_noise_level_db', models.FloatField(default=28.9, verbose_name='Уровень шума вентилятора, дБ')),
                ('airflow_cfm', models.IntegerField(default=70, verbose_name='Воздушный поток, CFM')),
                ('bearing_type', models.CharField(default='гидродинамический (FDB, S-FDB)', max_length=50, verbose_name='Тип подшипника')),
                ('connector_type', models.CharField(default='4-pin PWM', max_length=50, verbose_name='Тип коннектора')),
                ('speed_control', models.CharField(default='PWM', max_length=50, verbose_name='Регулятор оборотов')),
                ('lighting', models.BooleanField(default=False, verbose_name='Подсветка')),
                ('height_mm', models.IntegerField(default=151, verbose_name='Высота кулера, мм')),
                ('color_scheme', models.CharField(default='чёрный', max_length=50, verbose_name='Цвета оформления')),
                ('weight_kg', models.FloatField(default=0.65, verbose_name='Вес, кг')),
                ('warranty', models.IntegerField(default=12, verbose_name='Гарантия (мес.)')),
                ('manufacturer_website', models.URLField(default='www.idcooling.com', verbose_name='Сайт производителя')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/coolers/', verbose_name='Фото кулера')),
            ],
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название видеокарты')),
                ('type', models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'SPUCooler')], max_length=40)),
                ('interface', models.CharField(default='PCI Express 4.0', max_length=50, verbose_name='Интерфейс')),
                ('manufacturer_gpu', models.CharField(default='NVIDIA', max_length=100, verbose_name='Производитель видеопроцессора')),
                ('series', models.CharField(default='GeForce RTX 4060', max_length=50, verbose_name='Серия')),
                ('slots_occupied', models.IntegerField(default=2, verbose_name='Количество занимаемых слотов')),
                ('cooling_system', models.CharField(default='активная', max_length=50, verbose_name='Система охлаждения')),
                ('fan_count', models.IntegerField(default=2, verbose_name='Количество вентиляторов')),
                ('ports', models.CharField(default='HDMI, 3 x DisplayPort', max_length=100, verbose_name='Разъёмы')),
                ('gpu_architecture', models.CharField(default='nVidia Ada Lovelace', max_length=50, verbose_name='Архитектура графического процессора')),
                ('gpu_codename', models.CharField(default='AD107', max_length=50, verbose_name='Кодовое название графического процессора')),
                ('manufacturing_process', models.CharField(default='5 нм', max_length=50, verbose_name='Техпроцесс')),
                ('gpu_base_clock', models.IntegerField(default=1830, verbose_name='Частота графического процессора')),
                ('gpu_boost_clock', models.IntegerField(default=2505, verbose_name='Частота графического процессора (Boost)')),
                ('cuda_cores', models.IntegerField(default=3072, verbose_name='Число универсальных процессоров')),
                ('oc_version', models.BooleanField(default=True, verbose_name='OC версия')),
                ('sli_crossfire_support', models.BooleanField(default=False, verbose_name='Поддержка SLI/CrossFire')),
                ('directx_support', models.CharField(default='DirectX 12 Ultimate', max_length=50, verbose_name='Поддержка DirectX')),
                ('opengl_support', models.CharField(default='OpenGL 4.6', max_length=50, verbose_name='Поддержка OpenGL')),
                ('memory_size', models.IntegerField(default=8, verbose_name='Объём памяти')),
                ('memory_type', models.CharField(default='GDDR6', max_length=50, verbose_name='Тип памяти')),
                ('memory_bus', models.IntegerField(default=128, verbose_name='Шина памяти (разрядность)')),
                ('memory_bandwidth', models.IntegerField(default=272, verbose_name='Пропускная способность')),
                ('memory_clock', models.IntegerField(default=17000, verbose_name='Частота видеопамяти')),
                ('supported_monitors', models.IntegerField(default=4, verbose_name='Количество поддерживаемых мониторов')),
                ('max_resolution', models.CharField(default='7680x4320', max_length=50, verbose_name='Максимальное разрешение')),
                ('additional_power_needed', models.BooleanField(default=True, verbose_name='Необходимость дополнительного питания')),
                ('power_connector', models.CharField(default='8 pin', max_length=50, verbose_name='Разъём дополнительного питания')),
                ('recommended_psu_power', models.IntegerField(default=550, verbose_name='Рекомендуемая мощность блока питания')),
                ('tgp', models.IntegerField(default=115, verbose_name='TGP')),
                ('color_scheme', models.CharField(default='чёрный', max_length=50, verbose_name='Цвета оформления')),
                ('dimensions_mm', models.CharField(default='199 x 120 x 41 мм', max_length=50, verbose_name='Размеры (ШхВхГ), мм')),
                ('weight_kg', models.FloatField(default=0.6, verbose_name='Вес, кг')),
                ('warranty', models.IntegerField(default=36, verbose_name='Гарантия (мес.)')),
                ('manufacturer_website', models.URLField(default='www.msi.com', verbose_name='Сайт производителя')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/gpu/', verbose_name='Фото видеокарты')),
            ],
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название материнской платы')),
                ('type', models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'SPUCooler')], max_length=40)),
                ('socket', models.CharField(default='LGA 1700', max_length=50, verbose_name='Сокет')),
                ('chipset', models.CharField(default='Intel B760', max_length=50, verbose_name='Чипсет')),
                ('ram_type', models.CharField(default='DDR5', max_length=50, verbose_name='Тип ОЗУ')),
                ('max_ram', models.IntegerField(default=128, verbose_name='Максимальный объем ОЗУ, ГБ')),
                ('ram_slots', models.IntegerField(default=4, verbose_name='Количество слотов ОЗУ')),
                ('form_factor', models.CharField(default='ATX', max_length=50, verbose_name='Форм-фактор')),
                ('m2_slots', models.IntegerField(default=2, verbose_name='Количество слотов M.2')),
                ('sata_ports', models.IntegerField(default=4, verbose_name='Количество SATA портов')),
                ('pcie_version', models.CharField(default='PCIe 4.0', max_length=50, verbose_name='Версия PCIe')),
                ('usb_ports', models.CharField(default='PS/2, 4 x USB 2.0, 2 x USB 3.2 Gen2, USB 3.2 Gen2 Type-C', max_length=100, verbose_name='Порты USB')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/motherboards/', verbose_name='Фото материнской платы')),
                ('integrated_video', models.BooleanField(default=True, verbose_name='Интегрированное видео')),
                ('audio_controller', models.CharField(default='Realtek ALC897', max_length=100, verbose_name='Аудио-контроллер')),
                ('network_interface', models.CharField(default='2.5 Gigabit Ethernet, Wi-Fi, Bluetooth', max_length=100, verbose_name='Сетевой интерфейс')),
                ('network_controller', models.CharField(default='Realtek RTL8125BG', max_length=100, verbose_name='Сетевой контроллер')),
                ('power_phases', models.CharField(default='12+1+1', max_length=50, verbose_name='Количество фаз питания')),
                ('heatsink_on_power', models.BooleanField(default=True, verbose_name='Радиатор на подсистеме питания')),
                ('fan_connectors', models.IntegerField(default=5, verbose_name='Количество разъемов для вентиляторов корпуса')),
                ('atx_12v_connector', models.CharField(default='4-pin, 8-pin', max_length=50, verbose_name='Разъем питания ATX 12 В')),
                ('internal_usb_ports', models.CharField(default='2 x USB 2.0, USB 3.2 Gen1, USB 3.2 Gen1 Type-C', max_length=100, verbose_name='Внутренние порты USB')),
                ('argb_connectors', models.IntegerField(default=2, verbose_name='Коннекторы ARGB на плате')),
                ('rgb_connectors', models.IntegerField(default=1, verbose_name='Коннекторы RGB на плате')),
                ('color_scheme', models.CharField(default='серый, чёрный', max_length=100, verbose_name='Цвета оформления')),
                ('warranty', models.IntegerField(default=36, verbose_name='Гарантия (мес.)')),
                ('manufacturer_website', models.URLField(default='www.msi.com', verbose_name='Сайт производителя')),
            ],
        ),
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название операционной системы')),
                ('manufacturer', models.CharField(default='Microsoft', max_length=100, verbose_name='Производитель')),
                ('code', models.CharField(default='FQC-10547', max_length=100, verbose_name='Код производителя')),
                ('type', models.CharField(default='дистрибутив/лицензия', max_length=50, verbose_name='Тип комплектации')),
                ('line', models.CharField(default='Windows 11', max_length=50, verbose_name='Линейка')),
                ('release', models.CharField(default='Professional', max_length=50, verbose_name='Выпуск')),
                ('bit_version', models.CharField(default='64 bit', max_length=20, verbose_name='Битность')),
                ('supply_type', models.CharField(default='OEM (только в комплекте с ПК)', max_length=50, verbose_name='Тип поставки')),
                ('license_info', models.CharField(default='лицензия на 1 ПК', max_length=100, verbose_name='Лицензия')),
                ('website', models.URLField(default='www.microsoft.com', verbose_name='Сайт производителя')),
                ('warranty', models.IntegerField(blank=True, null=True, verbose_name='Гарантия (мес.)')),
            ],
        ),
        migrations.CreateModel(
            name='PSU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название блока питания')),
                ('type', models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'SPUCooler')], max_length=40)),
                ('power', models.IntegerField(default=750, verbose_name='Мощность, Вт')),
                ('efficiency_rating', models.CharField(default='Standard', max_length=50, verbose_name='Коэффициент эффективности')),
                ('modularity', models.CharField(blank=True, choices=[('Modular', 'Модульный'), ('Non-Modular', 'Немодульный'), ('Semi-Modular', 'Полумодульный')], max_length=50, null=True, verbose_name='Тип кабелей')),
                ('pcie_connectors', models.IntegerField(default=4, verbose_name='Количество разъемов PCIe')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/psu/', verbose_name='Фото блока питания')),
                ('protection_overvoltage', models.BooleanField(default=True, verbose_name='Защита от перенапряжения')),
                ('protection_overload', models.BooleanField(default=True, verbose_name='Защита от перегрузки')),
                ('protection_short_circuit', models.BooleanField(default=True, verbose_name='Защита от короткого замыкания')),
                ('motherboard_connector_length', models.IntegerField(default=55, verbose_name='Длина кабеля питания материнской платы (см)')),
                ('fan_size', models.IntegerField(default=120, verbose_name='Размер вентилятора')),
                ('website', models.URLField(default='www.deepcool.com', verbose_name='Сайт производителя')),
                ('warranty', models.IntegerField(default=36, verbose_name='Гарантия (мес.)')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название ОЗУ')),
                ('type', models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'SPUCooler')], max_length=40)),
                ('form_factor', models.CharField(default='DIMM', max_length=50, verbose_name='Форм-фактор')),
                ('memory_type', models.CharField(default='DDR5', max_length=50, verbose_name='Тип ОЗУ')),
                ('capacity', models.IntegerField(default=32, verbose_name='Объем ОЗУ, ГБ')),
                ('module_capacity', models.IntegerField(default=16, verbose_name='Объем одного модуля, ГБ')),
                ('kit_modules', models.IntegerField(default=2, verbose_name='Количество модулей в комплекте')),
                ('frequency', models.IntegerField(default=6000, verbose_name='Частота, МГц')),
                ('bandwidth', models.IntegerField(default=48000, verbose_name='Пропускная способность, Мб/с')),
                ('cas_latency', models.IntegerField(default=40, verbose_name='CAS Latency (CL)')),
                ('trcd', models.IntegerField(default=40, verbose_name='RAS to CAS Delay (tRCD)')),
                ('trp', models.IntegerField(default=40, verbose_name='Row Precharge Delay (tRP)')),
                ('voltage', models.FloatField(default=1.35, verbose_name='Напряжение питания, В')),
                ('xmp_support', models.BooleanField(default=True, verbose_name='Поддержка XMP')),
                ('cooling_system', models.CharField(default='пассивная (радиатор)', max_length=50, verbose_name='Система охлаждения')),
                ('module_height_mm', models.IntegerField(default=35, verbose_name='Высота модуля, мм')),
                ('color_scheme', models.CharField(default='чёрный', max_length=50, verbose_name='Цвета оформления')),
                ('dimensions_mm', models.CharField(default='133 x 35 x 7 мм', max_length=50, verbose_name='Размеры (ШхВхГ), мм')),
                ('warranty', models.IntegerField(default=36, verbose_name='Гарантия (мес.)')),
                ('manufacturer_website', models.URLField(default='www.kingston.com', verbose_name='Сайт производителя')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/ram/', verbose_name='Фото ОЗУ')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название накопителя')),
                ('type', models.CharField(choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'), ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'), ('spucooler', 'SPUCooler')], max_length=40)),
                ('storage_type', models.CharField(choices=[('HDD', 'HDD'), ('SSD', 'SSD'), ('NVMe', 'NVMe')], default='HDD', max_length=50, verbose_name='Тип накопителя')),
                ('form_factor', models.CharField(default='3.5"', max_length=50, verbose_name='Форм-фактор')),
                ('interface', models.CharField(default='SATA-III', max_length=50, verbose_name='Интерфейс подключения')),
                ('capacity_gb', models.IntegerField(default=8000, verbose_name='Емкость, ГБ')),
                ('cache_size', models.IntegerField(default=256, verbose_name='Объём буферной памяти, Мб')),
                ('rpm', models.IntegerField(default=7200, verbose_name='Скорость вращения шпинделя, об/мин')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/storage/', verbose_name='Фото накопителя')),
                ('warranty', models.IntegerField(default=12, verbose_name='Гарантия (мес.)')),
                ('manufacturer_website', models.URLField(default='www.seagate.com', verbose_name='Сайт производителя')),
            ],
        ),
    ]