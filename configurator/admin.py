from django.contrib import admin

# Register your models here.

from .models import *


class CPUAdmin(admin.ModelAdmin):
    exclude = ('product',)
class MotherboardAdmin(admin.ModelAdmin):
    exclude = ('product',)
class RAMAdmin(admin.ModelAdmin):
    exclude = ('product',)
class GPUAdmin(admin.ModelAdmin):
    exclude = ('product',)
class PSUAdmin(admin.ModelAdmin):
    exclude = ('product',)
class CaseAdmin(admin.ModelAdmin):
    exclude = ('product',)
class HDDAdmin(admin.ModelAdmin):
    exclude = ('product',)
class SSDAdmin(admin.ModelAdmin):
    exclude = ('product',)
class CPUCoolerAdmin(admin.ModelAdmin):
    exclude = ('product',)


admin.site.register(Product)
admin.site.register(CPU, CPUAdmin)
admin.site.register(Motherboard, MotherboardAdmin)
admin.site.register(RAM, RAMAdmin)
admin.site.register(GPU, GPUAdmin)
admin.site.register(PSU, PSUAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(HDD, HDDAdmin)
admin.site.register(SSD, SSDAdmin)
admin.site.register(CPUCooler, CPUCoolerAdmin)
admin.site.register(Build)
