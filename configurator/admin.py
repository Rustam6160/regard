from django.contrib import admin

# Register your models here.

from .models import *


class CPUAdmin(admin.ModelAdmin):
    # Скрыть поле product, так как оно будет автоматически заполняться
    exclude = ('product',)

admin.site.register(Product)
admin.site.register(CPU, CPUAdmin)
admin.site.register(Motherboard)
admin.site.register(RAM)
admin.site.register(GPU)
admin.site.register(PSU)
admin.site.register(Case)
admin.site.register(Storage)
admin.site.register(CPUCooler)
admin.site.register(Build)
