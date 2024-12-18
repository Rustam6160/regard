from django.http import JsonResponse
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, ListView
from .services import *



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
        return render(request, 'configurator/products.html', {'items': categories})




from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import CPU, Motherboard, RAM, GPU, PSU, Case, Storage, OS, CPUCooler


class ConfiguratorView(View):
    def get(self, request, selected_product_category=None, selected_product_id=None):
        delete = request.GET.get('delete')
        if delete:
            print(f"Удаление продукта с категорией: {selected_product_category}")
            print(f"Текущие выбранные продукты: {request.session.get('selected_products', {})}")

            if selected_product_category in request.session['selected_products']:
                del request.session['selected_products'][selected_product_category]
                request.session.modified = True

        # Восстановление выбора из сессии
        selected_products = {
            'cpu': CPU.objects.get(id=cpu_id) if (
                cpu_id := request.session.get('selected_products', {}).get('cpu')) else None,
            'motherboard': Motherboard.objects.get(id=mobo_id) if (
                mobo_id := request.session.get('selected_products', {}).get('motherboard')) else None,
            'ram': RAM.objects.get(id=ram_id) if (
                ram_id := request.session.get('selected_products', {}).get('ram')) else None,
            'gpu': GPU.objects.get(id=gpu_id) if (
                gpu_id := request.session.get('selected_products', {}).get('gpu')) else None,
            'psu': PSU.objects.get(id=psu_id) if (
                psu_id := request.session.get('selected_products', {}).get('psu')) else None,
            'case': Case.objects.get(id=case_id) if (
                case_id := request.session.get('selected_products', {}).get('case')) else None,
            'storage': Storage.objects.get(id=storage_id) if (
                storage_id := request.session.get('selected_products', {}).get('storage')) else None,
            'os': OS.objects.get(id=os_id) if (
                os_id := request.session.get('selected_products', {}).get('os')) else None,
            'cpucooler': CPUCooler.objects.get(id=cooler_id) if (
                cooler_id := request.session.get('selected_products', {}).get('cpucooler')) else None,
        }




        # Добавление нового продукта
        if not delete:
            print(77)
            if selected_product_id and selected_product_category:
                model_map = {
                    'cpu': CPU,
                    'motherboard': Motherboard,
                    'ram': RAM,
                    'gpu': GPU,
                    'psu': PSU,
                    'case': Case,
                    'storage': Storage,
                    'os': OS,
                    'cpucooler': CPUCooler,
                }
                if selected_product_category in model_map:
                    selected_product = get_object_or_404(model_map[selected_product_category], id=selected_product_id)
                    selected_products[selected_product_category] = selected_product

        # Сохранение обновленного выбора в сессии
        request.session['selected_products'] = {
            key: value.id if value else None for key, value in selected_products.items()
        }



        # Получение доступных продуктов и фильтрация
        available_products = {
            'cpu': CPU.objects.all(),
            'motherboard': Motherboard.objects.all(),
            'ram': RAM.objects.all(),
            'gpu': GPU.objects.all(),
            'psu': PSU.objects.all(),
            'case': Case.objects.all(),
            'storage': Storage.objects.all(),
            'os': OS.objects.all(),
            'cpucooler': CPUCooler.objects.all(),
        }

        # Фильтрация доступных продуктов
        if selected_products['cpu']:
            cpu = selected_products['cpu']
            available_products['motherboard'] = available_products['motherboard'].filter(socket=cpu.socket)
        if selected_products['motherboard']:
            motherboard = selected_products['motherboard']
            available_products['cpu'] = available_products['cpu'].filter(socket=motherboard.socket)
            available_products['ram'] = available_products['ram'].filter(memory_type=motherboard.ram_type)
            available_products['gpu'] = available_products['gpu'].filter(interface=motherboard.pcie_version)
            available_products['case'] = available_products['case'].filter(
                form_factor_support__icontains=motherboard.form_factor)
        if selected_products['ram']:
            ram = selected_products['ram']
            available_products['motherboard'] = available_products['motherboard'].filter(ram_type=ram.memory_type)
        if selected_products['gpu']:
            gpu = selected_products['gpu']
            available_products['motherboard'] = available_products['motherboard'].filter(pcie_version=gpu.interface)
            available_products['psu'] = available_products['psu'].filter(pcie_connectors__gte=1)
            available_products['case'] = available_products['case'].filter(max_gpu_length_mm__gte=gpu.dimensions_mm)
        if selected_products['case']:
            case = selected_products['case']
            available_products['gpu'] = available_products['gpu'].filter(dimensions_mm__lte=case.max_gpu_length_mm)
            supported_sizes = case.form_factor_support.split(', ')
            available_products['motherboard'] = available_products['motherboard'].filter(
                form_factor__in=supported_sizes)
        if selected_products['psu']:
            psu = selected_products['psu']
            available_products['gpu'] = available_products['gpu'].filter(additional_power_needed=True)

        return render(request, 'configurator/configurator.html', {
            'available_products': available_products,
            'selected_products': selected_products,
        })


class OrderComponents(View):
    def get(self, request):
        selected_products = {
            'cpu': CPU.objects.get(id=cpu_id) if (
                cpu_id := request.session.get('selected_products', {}).get('cpu')) else None,
            'motherboard': Motherboard.objects.get(id=mobo_id) if (
                mobo_id := request.session.get('selected_products', {}).get('motherboard')) else None,
            'ram': RAM.objects.get(id=ram_id) if (
                ram_id := request.session.get('selected_products', {}).get('ram')) else None,
            'gpu': GPU.objects.get(id=gpu_id) if (
                gpu_id := request.session.get('selected_products', {}).get('gpu')) else None,
            'psu': PSU.objects.get(id=psu_id) if (
                psu_id := request.session.get('selected_products', {}).get('psu')) else None,
            'case': Case.objects.get(id=case_id) if (
                case_id := request.session.get('selected_products', {}).get('case')) else None,
            'storage': Storage.objects.get(id=storage_id) if (
                storage_id := request.session.get('selected_products', {}).get('storage')) else None,
            'os': OS.objects.get(id=os_id) if (
                os_id := request.session.get('selected_products', {}).get('os')) else None,
            'cpucooler': CPUCooler.objects.get(id=cooler_id) if (
                cooler_id := request.session.get('selected_products', {}).get('cpucooler')) else None,
        }

        return render(request, 'configurator/order.html', context={"selected_products": selected_products})





