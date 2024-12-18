from django.db import models





class Product(models.Model):
    type = models.CharField(
        max_length=40,
        choices=[
            ('cpu', 'CPU'),
            ('motherboard', 'Motherboard'),
            ('ram', 'RAM'),
            ('gpu', 'GPU'),
            ('psu', 'PSU'),
            ('case', 'Case'),
            ('storage', 'Storage'),
            ('os', 'OS'),
            ('spucooler', 'SPUCooler')
        ]
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        abstract = True


# Модель для процессоров (CPU)
class CPU(Product):
    name = models.CharField(max_length=100, verbose_name="Название процессора")
    image = models.ImageField(upload_to='images/CPU/', null=True, blank=True, verbose_name="Фото CPU")
    manufacturer = models.CharField(max_length=100, verbose_name="Производитель", default="Intel")
    socket = models.CharField(max_length=50, verbose_name="Socket", default="LGA 1700")
    architecture = models.CharField(max_length=50, verbose_name="Архитектура", null=True, blank=True)
    cores = models.IntegerField(verbose_name="Количество ядер", default=4)
    threads = models.IntegerField(verbose_name="Количество потоков", null=True, blank=True)
    base_clock = models.FloatField(verbose_name="Тактовая частота", null=True, blank=True)
    turbo_clock = models.FloatField(verbose_name="Частота процессора в режиме Turbo", null=True, blank=True)
    tdp = models.IntegerField(verbose_name="Типичное тепловыделение", null=True, blank=True)
    release_date = models.CharField(max_length=50, verbose_name="Дата релиза", null=True, blank=True)

    def __str__(self):
        return self.name

# Модель для материнских плат (Motherboard)
class Motherboard(Product):
    name = models.CharField(max_length=100, verbose_name="Название материнской платы")
    socket = models.CharField(max_length=50, verbose_name="Сокет", default="LGA 1700")
    chipset = models.CharField(max_length=50, verbose_name="Чипсет", default="Intel B760")
    ram_type = models.CharField(max_length=50, verbose_name="Тип ОЗУ", default="DDR4")
    max_ram = models.IntegerField(verbose_name="Максимальный объем ОЗУ, ГБ", default=128)
    ram_slots = models.IntegerField(verbose_name="Количество слотов ОЗУ", default=4)
    form_factor = models.CharField(max_length=50, verbose_name="Форм-фактор", default="ATX")
    m2_slots = models.IntegerField(verbose_name="Количество слотов M.2", default=2)
    sata_ports = models.IntegerField(verbose_name="Количество SATA портов", default=4)
    pcie_version = models.CharField(max_length=50, verbose_name="Версия PCIe", default="PCI Express 4.0")
    image = models.ImageField(upload_to='images/motherboards/', null=True, blank=True, verbose_name="Фото материнской платы")

    def __str__(self):
        return self.name

# Модель для оперативной памяти (RAM)
class RAM(Product):
    name = models.CharField(max_length=100, verbose_name="Название ОЗУ")
    form_factor = models.CharField(max_length=50, verbose_name="Форм-фактор", default="DIMM")
    memory_type = models.CharField(max_length=50, verbose_name="Тип ОЗУ", default="DDR4")
    capacity = models.IntegerField(verbose_name="Объем ОЗУ, ГБ", default=8)
    module_capacity = models.IntegerField(verbose_name="Объем одного модуля, ГБ", default=16)
    kit_modules = models.IntegerField(verbose_name="Количество модулей в комплекте", default=2)
    frequency = models.IntegerField(verbose_name="Частота, МГц", default=6000)
    cas_latency = models.IntegerField(verbose_name="CAS Latency (CL)", default=40)
    voltage = models.FloatField(verbose_name="Напряжение питания, В", default=1.35)
    xmp_support = models.BooleanField(verbose_name="Поддержка XMP", default=True)
    image = models.ImageField(upload_to='images/ram/', null=True, blank=True, verbose_name="Фото ОЗУ")

    def __str__(self):
        return self.name

# Модель для видеокарт (GPU)
class GPU(Product):
    name = models.CharField(max_length=100, verbose_name="Название видеокарты")
    interface = models.CharField(max_length=50, verbose_name="Интерфейс", default="PCI Express 4.0")
    manufacturer_gpu = models.CharField(max_length=100, verbose_name="Производитель видеопроцессора", default="unknown")
    series = models.CharField(max_length=50, verbose_name="Серия", default="unknown")
    memory_size = models.IntegerField(verbose_name="Объём памяти", default=8)
    memory_type = models.CharField(max_length=50, verbose_name="Тип памяти", default="GDDR6")
    memory_bus = models.IntegerField(verbose_name="Шина памяти (разрядность)", default=128)
    dimensions_mm = models.IntegerField(verbose_name="Шырина (длина) мм", default=199)
    gpu_base_clock = models.IntegerField(verbose_name="Частота графического процессора", default=1830)
    gpu_boost_clock = models.IntegerField(verbose_name="Частота графического процессора (Boost)", default=2505)
    cuda_cores = models.IntegerField(verbose_name="Число универсальных процессоров", default=3072)
    recommended_psu_power = models.IntegerField(verbose_name="Рекомендуемая мощность блока питания", default=550)
    tgp = models.IntegerField(verbose_name="TGP", default=115)
    image = models.ImageField(upload_to='images/gpu/', null=True, blank=True, verbose_name="Фото видеокарты")

    def __str__(self):
        return self.name

# Модель для блоков питания (PSU)
class PSU(Product):
    name = models.CharField(max_length=100, verbose_name="Название блока питания")
    power = models.IntegerField(verbose_name="Мощность, Вт", default=750)
    efficiency_rating = models.CharField(max_length=50, verbose_name="Коэффициент эффективности", default="Standard")
    modularity = models.CharField(
        max_length=50,
        choices=[
            ("Modular", "Модульный"),
            ("Non-Modular", "Немодульный"),
            ("Semi-Modular", "Полумодульный")
        ],
        verbose_name="Тип кабелей",
        null=True,
        blank=True
    )
    pcie_connectors = models.IntegerField(verbose_name="Количество разъемов PCIe", default=4)
    image = models.ImageField(upload_to='images/psu/', null=True, blank=True, verbose_name="Фото блока питания")

    def __str__(self):
        return self.name

# Модель для корпусов (Case)
class Case(Product):
    name = models.CharField(max_length=100, verbose_name="Название корпуса")
    image = models.ImageField(upload_to='images/cases/', null=True, blank=True, verbose_name="Фото корпуса")

    # Ключевые параметры для сравнения
    max_gpu_length_mm = models.IntegerField(verbose_name="Максимальная длина видеокарты, мм", default=315)
    max_cpu_cooler_height_mm = models.IntegerField(verbose_name="Максимальная высота кулера, мм", default=163)
    form_factor_support = models.CharField(max_length=100, verbose_name="Поддерживаемые форм-факторы материнских плат", default="ATX, mATX, Mini-ITX")
    psu_type = models.CharField(max_length=50, verbose_name="Тип блока питания (например, ATX, SFX)", default="без БП")
    drive_bays = models.CharField(max_length=100, verbose_name="Отсеки для накопителей (например, 2x3.5', 2x2.5')", default="2.5\" - 2, 3.5\" - 2")
    fan_slots = models.BooleanField(verbose_name="Места для вентиляторов", default=True)
    bottom_fans = models.CharField(max_length=50, verbose_name="Вентиляторы на нижней панели", default="2 x 120 мм")
    top_fans = models.CharField(max_length=50, verbose_name="Вентиляторы на верхней панели", default="2 x 120 мм")
    rgb_lighting = models.BooleanField(verbose_name="Подсветка корпуса", default=True)
    liquid_cooling_support = models.BooleanField(verbose_name="Возможность установки СЖО", default=True)
    dimensions = models.CharField(max_length=50, verbose_name="Размеры (ШхВхГ)", default="204 x 446 x 396 мм")
    weight_kg = models.FloatField(verbose_name="Вес", default=4.7)
    warranty = models.IntegerField(verbose_name="Гарантия (мес.)", default=12)

    def __str__(self):
        return self.name

# Модель для накопителей (Storage)
class Storage(Product):
    name = models.CharField(max_length=100, verbose_name="Название накопителя")
    storage_type = models.CharField(max_length=50, choices=[("HDD", "HDD"), ("SSD", "SSD"), ("NVMe", "NVMe")], verbose_name="Тип накопителя", default="HDD")
    capacity_gb = models.IntegerField(verbose_name="Емкость, ГБ", default=8000)
    rpm = models.IntegerField(verbose_name="Скорость вращения шпинделя, об/мин", null=True, blank=True)  # Только для HDD
    image = models.ImageField(upload_to='images/storage/', null=True, blank=True, verbose_name="Фото накопителя")

    # Дополнительные параметры для сравнения
    form_factor = models.CharField(max_length=50, verbose_name="Форм-фактор", default="3.5\"")
    interface = models.CharField(max_length=50, verbose_name="Интерфейс подключения", default="SATA-III")
    warranty = models.IntegerField(verbose_name="Гарантия (мес.)", default=12)

    def __str__(self):
        return self.name

# Модель операционной системы
class OS(Product):
    name = models.CharField(max_length=100, verbose_name="Название операционной системы")
    line = models.CharField(max_length=50, verbose_name="Линейка", default="Windows 11")
    release = models.CharField(max_length=50, verbose_name="Выпуск", default="Professional")
    bit_version = models.CharField(max_length=20, verbose_name="Битность", default="64 bit")
    supply_type = models.CharField(max_length=50, verbose_name="Тип поставки", default="OEM (только в комплекте с ПК)")
    image = models.ImageField(upload_to='images/os/', null=True, blank=True, verbose_name="Фото операционной системы")

    def __str__(self):
        return self.name



class CPUCooler(Product):
    name = models.CharField(max_length=100, verbose_name="Название кулера")
    socket_compatibility = models.CharField(max_length=255, verbose_name="Совместимые сокеты", default="LGA 115x/1200, LGA 1700, 1851, AM4, AM5")
    cooler_type = models.CharField(max_length=50, verbose_name="Тип системы охлаждения", default="активная")
    max_power_dissipation = models.IntegerField(verbose_name="Максимальная рассеиваемая мощность, Вт", default=220)
    fan_count = models.IntegerField(verbose_name="Количество вентиляторов", default=1)
    fan_size_mm = models.CharField(max_length=50, verbose_name="Размеры вентилятора, мм", default="120x120 мм")
    fan_speed_rpm = models.CharField(max_length=50, verbose_name="Скорость вращения вентилятора", default="600-1500 об/мин")
    fan_noise_level_db = models.FloatField(verbose_name="Уровень шума вентилятора, дБ", default=28.9)
    airflow_cfm = models.IntegerField(verbose_name="Воздушный поток, CFM", default=70)
    speed_control = models.CharField(max_length=50, verbose_name="Регулятор оборотов", default="PWM")
    lighting = models.BooleanField(verbose_name="Подсветка", default=False)
    height_mm = models.IntegerField(verbose_name="Высота кулера, мм", default=151)
    weight_kg = models.FloatField(verbose_name="Вес, кг", default=0.65)
    image = models.ImageField(upload_to='images/coolers/', null=True, blank=True, verbose_name="Фото кулера")

    def __str__(self):
        return self.name



