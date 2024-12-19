from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(CPU)
admin.site.register(Motherboard)
admin.site.register(RAM)
admin.site.register(GPU)
admin.site.register(PSU)
admin.site.register(Case)
admin.site.register(Storage)
admin.site.register(Build)