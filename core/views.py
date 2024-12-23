from django.http import JsonResponse
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from configurator.models import *


class ProductView(View):
    def get(self, request):
        # Формирование контекста с категориями и их объектами
        categories = {
            "cpu": CPU.objects.all(),
            "motherboard": Motherboard.objects.all(),
            "ram": RAM.objects.all(),
            "gpu": GPU.objects.all(),
            "psu": PSU.objects.all(),
            "case": Case.objects.all(),
            "storage": Storage.objects.all(),
            "os": OS.objects.all(),
            "cpucooler": CPUCooler.objects.all(),
        }
        return render(request, 'core/products.html', {'items': categories})