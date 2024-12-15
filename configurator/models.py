from django.db import models










# Модель для процессоров (CPU)
class CPU(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название процессора")
    type = models.CharField(max_length=40,
                            choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'),
                                     ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'), ('os', 'OS'),
                                     ('spucooler', 'SPUCooler')])

    manufacturer = models.CharField(max_length=100, verbose_name="Производитель", default="Intel")
    code = models.CharField(max_length=100, verbose_name="Код производителя", default="CM8071504555318/CM8071504650609")
    line = models.CharField(max_length=50, verbose_name="Линейка", default="Core i5")
    model = models.CharField(max_length=50, verbose_name="Модель", default="12400F")
    socket = models.CharField(max_length=50, verbose_name="Socket", default="LGA 1700")
    architecture = models.CharField(max_length=50, verbose_name="Архитектура", null=True, blank=True)
    core = models.CharField(max_length=50, verbose_name="Ядро", default="Golden Cove")
    cores = models.IntegerField(verbose_name="Количество ядер", default=6)
    threads = models.IntegerField(verbose_name="Количество потоков", null=True, blank=True)
    base_clock = models.FloatField(verbose_name="Тактовая частота", default=2500)
    turbo_clock = models.FloatField(verbose_name="Частота процессора в режиме Turbo", default=4400)
    bus_speed = models.CharField(max_length=50, verbose_name="Частота шины", null=True, blank=True)
    multiplier = models.IntegerField(verbose_name="Коэффициент умножения", null=True, blank=True)
    integrated_gpu = models.BooleanField(verbose_name="Интегрированное графическое ядро", default=False)
    l1_cache = models.FloatField(verbose_name="Объём кэша L1", null=True, blank=True)
    l2_cache = models.FloatField(verbose_name="Объём кэша L2", null=True, blank=True)
    l3_cache = models.FloatField(verbose_name="Объём кэша L3", null=True, blank=True)
    process_technology = models.CharField(max_length=50, verbose_name="Технологический процесс", null=True, blank=True)
    max_temp = models.IntegerField(verbose_name="Максимальная рабочая температура", null=True, blank=True)
    tdp = models.IntegerField(verbose_name="Типичное тепловыделение", null=True, blank=True)
    technologies = models.TextField(verbose_name="Технологии", null=True, blank=True)
    cooler_included = models.BooleanField(verbose_name="Кулер в комплекте", default=False)
    release_date = models.CharField(max_length=50, verbose_name="Дата релиза", null=True, blank=True)
    supply_type = models.CharField(max_length=50, verbose_name="Тип поставки", default="OEM (без кулера)")
    warranty = models.IntegerField(verbose_name="Гарантия (мес.)", default=12)
    website = models.URLField(verbose_name="Сайт производителя", default="www.intel.com")

    def __str__(self):
        return self.name

# Модель для материнских плат (Motherboard)
class Motherboard(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название материнской платы")
    type = models.CharField(max_length=40,
                            choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'),
                                     ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'),
                                     ('os', 'OS'),
                                     ('spucooler', 'SPUCooler')])
    socket = models.CharField(max_length=50, verbose_name="Сокет", default="LGA 1700")
    chipset = models.CharField(max_length=50, verbose_name="Чипсет", default="Intel B760")
    ram_type = models.CharField(max_length=50, verbose_name="Тип ОЗУ", default="DDR5")
    max_ram = models.IntegerField(verbose_name="Максимальный объем ОЗУ, ГБ", default=128)  # Примерное значение
    ram_slots = models.IntegerField(verbose_name="Количество слотов ОЗУ", default=4)
    form_factor = models.CharField(max_length=50, verbose_name="Форм-фактор", default="ATX")
    m2_slots = models.IntegerField(verbose_name="Количество слотов M.2", default=2)
    sata_ports = models.IntegerField(verbose_name="Количество SATA портов", default=4)
    pcie_version = models.CharField(max_length=50, verbose_name="Версия PCIe", default="PCIe 4.0")
    usb_ports = models.CharField(max_length=100, verbose_name="Порты USB",
                                 default="PS/2, 4 x USB 2.0, 2 x USB 3.2 Gen2, USB 3.2 Gen2 Type-C")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", null=True,
                                blank=True)  # Нужно указать цену
    image = models.ImageField(upload_to='images/motherboards/', null=True, blank=True,
                              verbose_name="Фото материнской платы")

    # Дополнительные характеристики
    integrated_video = models.BooleanField(verbose_name="Интегрированное видео", default=True)
    audio_controller = models.CharField(max_length=100, verbose_name="Аудио-контроллер", default="Realtek ALC897")
    network_interface = models.CharField(max_length=100, verbose_name="Сетевой интерфейс",
                                         default="2.5 Gigabit Ethernet, Wi-Fi, Bluetooth")
    network_controller = models.CharField(max_length=100, verbose_name="Сетевой контроллер",
                                          default="Realtek RTL8125BG")
    power_phases = models.CharField(max_length=50, verbose_name="Количество фаз питания", default="12+1+1")
    heatsink_on_power = models.BooleanField(verbose_name="Радиатор на подсистеме питания", default=True)
    fan_connectors = models.IntegerField(verbose_name="Количество разъемов для вентиляторов корпуса", default=5)
    atx_12v_connector = models.CharField(max_length=50, verbose_name="Разъем питания ATX 12 В", default="4-pin, 8-pin")
    internal_usb_ports = models.CharField(max_length=100, verbose_name="Внутренние порты USB",
                                          default="2 x USB 2.0, USB 3.2 Gen1, USB 3.2 Gen1 Type-C")
    argb_connectors = models.IntegerField(verbose_name="Коннекторы ARGB на плате", default=2)
    rgb_connectors = models.IntegerField(verbose_name="Коннекторы RGB на плате", default=1)
    color_scheme = models.CharField(max_length=100, verbose_name="Цвета оформления", default="серый, чёрный")
    warranty = models.IntegerField(verbose_name="Гарантия (мес.)", default=36)
    manufacturer_website = models.URLField(verbose_name="Сайт производителя", default="www.msi.com")

    def __str__(self):
        return self.name

# Модель для оперативной памяти (RAM)
class RAM(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название ОЗУ")
    type = models.CharField(max_length=40,
                            choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'),
                                     ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'),
                                     ('os', 'OS'),
                                     ('spucooler', 'SPUCooler')])
    form_factor = models.CharField(max_length=50, verbose_name="Форм-фактор", default="DIMM")
    memory_type = models.CharField(max_length=50, verbose_name="Тип ОЗУ", default="DDR5")
    capacity = models.IntegerField(verbose_name="Объем ОЗУ, ГБ", default=32)
    module_capacity = models.IntegerField(verbose_name="Объем одного модуля, ГБ", default=16)
    kit_modules = models.IntegerField(verbose_name="Количество модулей в комплекте", default=2)
    frequency = models.IntegerField(verbose_name="Частота, МГц", default=6000)
    bandwidth = models.IntegerField(verbose_name="Пропускная способность, Мб/с", default=48000)
    cas_latency = models.IntegerField(verbose_name="CAS Latency (CL)", default=40)
    trcd = models.IntegerField(verbose_name="RAS to CAS Delay (tRCD)", default=40)
    trp = models.IntegerField(verbose_name="Row Precharge Delay (tRP)", default=40)
    voltage = models.FloatField(verbose_name="Напряжение питания, В", default=1.35)
    xmp_support = models.BooleanField(verbose_name="Поддержка XMP", default=True)
    cooling_system = models.CharField(max_length=50, verbose_name="Система охлаждения", default="пассивная (радиатор)")
    module_height_mm = models.IntegerField(verbose_name="Высота модуля, мм", default=35)
    color_scheme = models.CharField(max_length=50, verbose_name="Цвета оформления", default="чёрный")
    dimensions_mm = models.CharField(max_length=50, verbose_name="Размеры (ШхВхГ), мм", default="133 x 35 x 7 мм")
    warranty = models.IntegerField(verbose_name="Гарантия (мес.)", default=36)
    manufacturer_website = models.URLField(verbose_name="Сайт производителя", default="www.kingston.com")
    image = models.ImageField(upload_to='images/ram/', null=True, blank=True, verbose_name="Фото ОЗУ")

    def __str__(self):
        return self.name

# Модель для видеокарт (GPU)
class GPU(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название видеокарты")
    type = models.CharField(max_length=40,
                            choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'),
                                     ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'),
                                     ('os', 'OS'),
                                     ('spucooler', 'SPUCooler')])
    interface = models.CharField(max_length=50, verbose_name="Интерфейс", default="PCI Express 4.0")
    manufacturer_gpu = models.CharField(max_length=100, verbose_name="Производитель видеопроцессора", default="NVIDIA")
    series = models.CharField(max_length=50, verbose_name="Серия", default="GeForce RTX 4060")
    slots_occupied = models.IntegerField(verbose_name="Количество занимаемых слотов", default=2)
    cooling_system = models.CharField(max_length=50, verbose_name="Система охлаждения", default="активная")
    fan_count = models.IntegerField(verbose_name="Количество вентиляторов", default=2)
    ports = models.CharField(max_length=100, verbose_name="Разъёмы", default="HDMI, 3 x DisplayPort")
    gpu_architecture = models.CharField(max_length=50, verbose_name="Архитектура графического процессора", default="nVidia Ada Lovelace")
    gpu_codename = models.CharField(max_length=50, verbose_name="Кодовое название графического процессора", default="AD107")
    manufacturing_process = models.CharField(max_length=50, verbose_name="Техпроцесс", default="5 нм")
    gpu_base_clock = models.IntegerField(verbose_name="Частота графического процессора", default=1830)
    gpu_boost_clock = models.IntegerField(verbose_name="Частота графического процессора (Boost)", default=2505)
    cuda_cores = models.IntegerField(verbose_name="Число универсальных процессоров", default=3072)
    oc_version = models.BooleanField(verbose_name="OC версия", default=True)
    sli_crossfire_support = models.BooleanField(verbose_name="Поддержка SLI/CrossFire", default=False)
    directx_support = models.CharField(max_length=50, verbose_name="Поддержка DirectX", default="DirectX 12 Ultimate")
    opengl_support = models.CharField(max_length=50, verbose_name="Поддержка OpenGL", default="OpenGL 4.6")
    memory_size = models.IntegerField(verbose_name="Объём памяти", default=8)
    memory_type = models.CharField(max_length=50, verbose_name="Тип памяти", default="GDDR6")
    memory_bus = models.IntegerField(verbose_name="Шина памяти (разрядность)", default=128)
    memory_bandwidth = models.IntegerField(verbose_name="Пропускная способность", default=272)
    memory_clock = models.IntegerField(verbose_name="Частота видеопамяти", default=17000)
    supported_monitors = models.IntegerField(verbose_name="Количество поддерживаемых мониторов", default=4)
    max_resolution = models.CharField(max_length=50, verbose_name="Максимальное разрешение", default="7680x4320")
    additional_power_needed = models.BooleanField(verbose_name="Необходимость дополнительного питания", default=True)
    power_connector = models.CharField(max_length=50, verbose_name="Разъём дополнительного питания", default="8 pin")
    recommended_psu_power = models.IntegerField(verbose_name="Рекомендуемая мощность блока питания", default=550)
    tgp = models.IntegerField(verbose_name="TGP", default=115)
    color_scheme = models.CharField(max_length=50, verbose_name="Цвета оформления", default="чёрный")
    dimensions_mm = models.CharField(max_length=50, verbose_name="Размеры (ШхВхГ), мм", default="199 x 120 x 41 мм")
    weight_kg = models.FloatField(verbose_name="Вес, кг", default=0.6)
    warranty = models.IntegerField(verbose_name="Гарантия (мес.)", default=36)
    manufacturer_website = models.URLField(verbose_name="Сайт производителя", default="www.msi.com")
    image = models.ImageField(upload_to='images/gpu/', null=True, blank=True, verbose_name="Фото видеокарты")

    def __str__(self):
        return self.name

# Модель для блоков питания (PSU)
class PSU(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название блока питания")
    type = models.CharField(max_length=40,
                            choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'),
                                     ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'),
                                     ('os', 'OS'),
                                     ('spucooler', 'SPUCooler')])
    power = models.IntegerField(verbose_name="Мощность, Вт", default=750)
    efficiency_rating = models.CharField(max_length=50, verbose_name="Коэффициент эффективности", default="Standard")
    modularity = models.CharField(max_length=50, choices=[("Modular", "Модульный"), ("Non-Modular", "Немодульный"), ("Semi-Modular", "Полумодульный")], verbose_name="Тип кабелей", null=True, blank=True)
    pcie_connectors = models.IntegerField(verbose_name="Количество разъемов PCIe", default=4)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", null=True, blank=True)
    image = models.ImageField(upload_to='images/psu/', null=True, blank=True, verbose_name="Фото блока питания")
    protection_overvoltage = models.BooleanField(verbose_name="Защита от перенапряжения", default=True)
    protection_overload = models.BooleanField(verbose_name="Защита от перегрузки", default=True)
    protection_short_circuit = models.BooleanField(verbose_name="Защита от короткого замыкания", default=True)
    motherboard_connector_length = models.IntegerField(verbose_name="Длина кабеля питания материнской платы (см)", default=55)
    fan_size = models.IntegerField(verbose_name="Размер вентилятора", default=120)
    website = models.URLField(verbose_name="Сайт производителя", default="www.deepcool.com")
    warranty = models.IntegerField(verbose_name="Гарантия (мес.)", default=36)

    def __str__(self):
        return self.name

# Модель для корпусов (Case)
class Case(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название корпуса")
    type = models.CharField(max_length=40,
                            choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'),
                                     ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'),
                                     ('os', 'OS'),
                                     ('spucooler', 'SPUCooler')])
    form_factor_support = models.CharField(max_length=100, verbose_name="Поддерживаемые форм-факторы материнских плат", default="ATX, mATX, Mini-ITX")
    max_gpu_length_mm = models.IntegerField(verbose_name="Максимальная длина видеокарты, мм", default=315)
    max_cpu_cooler_height_mm = models.IntegerField(verbose_name="Максимальная высота кулера, мм", default=163)
    drive_bays = models.CharField(max_length=100, verbose_name="Отсеки для накопителей (например, 2x3.5', 2x2.5')", default="2.5\" - 2, 3.5\" - 2")
    psu_type = models.CharField(max_length=50, verbose_name="Тип блока питания (например, ATX, SFX)", default="без БП")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", null=True, blank=True)  # Цена не указана
    image = models.ImageField(upload_to='images/cases/', null=True, blank=True, verbose_name="Фото корпуса")

    # Дополнительные характеристики
    material = models.CharField(max_length=50, verbose_name="Материал корпуса", default="сталь")
    side_window = models.BooleanField(verbose_name="Наличие окна на боковой стенке", default=True)
    window_material = models.CharField(max_length=50, verbose_name="Материал окна", default="закалённое стекло")
    expansion_slots = models.IntegerField(verbose_name="Количество слотов расширения", default=7)
    hdd_mounting = models.CharField(max_length=50, verbose_name="Размещение HDD", default="поперечное")
    max_psu_length_mm = models.IntegerField(verbose_name="Максимальная длина БП", default=180)
    front_panel_ports = models.CharField(max_length=100, verbose_name="Интерфейсы на лицевой панели", default="2 x USB 2.0, USB 3.0, аудио")
    fan_slots = models.BooleanField(verbose_name="Места для вентиляторов", default=True)
    bottom_fans = models.CharField(max_length=50, verbose_name="Вентиляторы на нижней панели", default="2 x 120 мм")
    top_fans = models.CharField(max_length=50, verbose_name="Вентиляторы на верхней панели", default="2 x 120 мм")
    rear_fan = models.CharField(max_length=50, verbose_name="Вентилятор на задней панели", default="120 мм")
    front_fans = models.CharField(max_length=100, verbose_name="Вентиляторы на передней панели", default="3 x 140 мм")
    rgb_lighting = models.BooleanField(verbose_name="Подсветка корпуса", default=True)
    rgb_type = models.CharField(max_length=50, verbose_name="Тип подсветки", default="FRGB (Fixed RGB)")
    liquid_cooling_support = models.BooleanField(verbose_name="Возможность установки СЖО", default=True)
    dust_filters = models.CharField(max_length=100, verbose_name="Пылевой фильтр", default="на верхней панели, на нижней панели")
    additional_info = models.CharField(max_length=200, verbose_name="Дополнительная информация", default="посадочные места передней панели совместимы с двумя вентиляторами 180 мм или тремя 120 мм")
    color_scheme = models.CharField(max_length=50, verbose_name="Цвета оформления", default="чёрный")
    dimensions = models.CharField(max_length=50, verbose_name="Размеры (ШхВхГ)", default="204 x 446 x 396 мм")
    weight_kg = models.FloatField(verbose_name="Вес", default=4.7)
    warranty = models.IntegerField(verbose_name="Гарантия (мес.)", default=12)
    manufacturer_website = models.URLField(verbose_name="Сайт производителя", default="www.zalman.com")

    def __str__(self):
        return self.name

# Модель для накопителей (Storage)
class Storage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название накопителя")
    type = models.CharField(max_length=40,
                            choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'),
                                     ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'),
                                     ('os', 'OS'),
                                     ('spucooler', 'SPUCooler')])
    storage_type = models.CharField(max_length=50, choices=[("HDD", "HDD"), ("SSD", "SSD"), ("NVMe", "NVMe")], verbose_name="Тип накопителя", default="HDD")
    form_factor = models.CharField(max_length=50, verbose_name="Форм-фактор", default="3.5\"")
    interface = models.CharField(max_length=50, verbose_name="Интерфейс подключения", default="SATA-III")
    capacity_gb = models.IntegerField(verbose_name="Емкость, ГБ", default=8000)
    cache_size = models.IntegerField(verbose_name="Объём буферной памяти, Мб", default=256)
    rpm = models.IntegerField(verbose_name="Скорость вращения шпинделя, об/мин", default=7200)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", null=True, blank=True)
    image = models.ImageField(upload_to='images/storage/', null=True, blank=True, verbose_name="Фото накопителя")
    warranty = models.IntegerField(verbose_name="Гарантия (мес.)", default=12)
    manufacturer_website = models.URLField(verbose_name="Сайт производителя", default="www.seagate.com")

    def __str__(self):
        return self.name

# Модель операционной системы
class OS(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название операционной системы")
    type = models.CharField(max_length=40,
                            choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'),
                                     ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'),
                                     ('os', 'OS'),
                                     ('spucooler', 'SPUCooler')])
    manufacturer = models.CharField(max_length=100, verbose_name="Производитель", default="Microsoft")
    code = models.CharField(max_length=100, verbose_name="Код производителя", default="FQC-10547")
    type = models.CharField(max_length=50, verbose_name="Тип комплектации", default="дистрибутив/лицензия")
    line = models.CharField(max_length=50, verbose_name="Линейка", default="Windows 11")
    release = models.CharField(max_length=50, verbose_name="Выпуск", default="Professional")
    bit_version = models.CharField(max_length=20, verbose_name="Битность", default="64 bit")
    supply_type = models.CharField(max_length=50, verbose_name="Тип поставки", default="OEM (только в комплекте с ПК)")
    license_info = models.CharField(max_length=100, verbose_name="Лицензия", default="лицензия на 1 ПК")
    website = models.URLField(verbose_name="Сайт производителя", default="www.microsoft.com")
    warranty = models.IntegerField(verbose_name="Гарантия (мес.)", null=True, blank=True)

    def __str__(self):
        return self.name



class CPUCooler(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название кулера")
    type = models.CharField(max_length=40,
                            choices=[('cpu', 'CPU'), ('motherboard', 'Motherboard'), ('ram', 'RAM'),
                                     ('gpu', 'GPU'), ('psu', 'PSU'), ('case', 'Case'), ('storage', 'Storage'),
                                     ('os', 'OS'),
                                     ('spucooler', 'SPUCooler')])
    socket_compatibility = models.CharField(max_length=255, verbose_name="Совместимые сокеты", default="LGA 115x/1200, LGA 1700, 1851, AM4, AM5")
    cooler_type = models.CharField(max_length=50, verbose_name="Тип системы охлаждения", default="активная")
    max_power_dissipation = models.IntegerField(verbose_name="Максимальная рассеиваемая мощность, Вт", default=220)
    heatpipes = models.BooleanField(verbose_name="Тепловые трубки", default=True)
    radiator_material = models.CharField(max_length=50, verbose_name="Материал радиатора", default="алюминий")
    base_material = models.CharField(max_length=50, verbose_name="Материал основания", default="алюминий/медь")
    fan_count = models.IntegerField(verbose_name="Количество вентиляторов", default=1)
    fan_size_mm = models.CharField(max_length=50, verbose_name="Размеры вентилятора, мм", default="120x120 мм")
    fan_speed_rpm = models.CharField(max_length=50, verbose_name="Скорость вращения вентилятора", default="600-1500 об/мин")
    fan_noise_level_db = models.FloatField(verbose_name="Уровень шума вентилятора, дБ", default=28.9)
    airflow_cfm = models.IntegerField(verbose_name="Воздушный поток, CFM", default=70)
    bearing_type = models.CharField(max_length=50, verbose_name="Тип подшипника", default="гидродинамический (FDB, S-FDB)")
    connector_type = models.CharField(max_length=50, verbose_name="Тип коннектора", default="4-pin PWM")
    speed_control = models.CharField(max_length=50, verbose_name="Регулятор оборотов", default="PWM")
    lighting = models.BooleanField(verbose_name="Подсветка", default=False)
    height_mm = models.IntegerField(verbose_name="Высота кулера, мм", default=151)
    color_scheme = models.CharField(max_length=50, verbose_name="Цвета оформления", default="чёрный")
    weight_kg = models.FloatField(verbose_name="Вес, кг", default=0.65)
    warranty = models.IntegerField(verbose_name="Гарантия (мес.)", default=12)
    manufacturer_website = models.URLField(verbose_name="Сайт производителя", default="www.idcooling.com")
    image = models.ImageField(upload_to='images/coolers/', null=True, blank=True, verbose_name="Фото кулера")

    def __str__(self):
        return self.name



