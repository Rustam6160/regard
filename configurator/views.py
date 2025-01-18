from django.http import JsonResponse
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *




class ConfiguratorView(View):
    def get(self, request, selected_product_category=None, selected_product_id=None):
        delete = request.GET.get('delete')
        clear = request.GET.get('clear')

        if clear:
            if request.session.get('selected_products'):
                del request.session['selected_products']
                request.session.modified=True

        if delete:
            print(f"Удаление продукта с категорией: {selected_product_category}")
            print(f"Текущие выбранные продукты: {request.session.get('selected_products', {})}")

            if selected_product_category in request.session['selected_products']:
                del request.session['selected_products'][selected_product_category]
                request.session.modified = True

        # Восстановление выбора из сессии
        selected_products = selected_products_from_session(request)

        # Добавление нового продукта
        if not delete:
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

        selected_products_price = 0
        for key, selected_product in selected_products.items():
            if selected_product:
                selected_products_price += selected_product.product.price

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
            available_products['gpu'] = available_products['gpu'].filter(recommended_psu_power__lt=psu.power)

        return render(request, 'configurator/configurator.html', {
            'available_products': available_products,
            'selected_products': selected_products,
            'selected_products_price': selected_products_price,
        })


@method_decorator(login_required, name='dispatch')
class SaveMyBuild(View):
    def get(self, request):
        selected_products = selected_products_from_session(request)
        selected_products_price = 0
        for key, selected_product in selected_products.items():
            if selected_product:
                selected_products_price += selected_product.product.price

        Build.objects.create(author=request.user, cpu=selected_products['cpu'],
                             motherboard=selected_products['motherboard'],
                             ram=selected_products['ram'],
                             gpu=selected_products['gpu'],
                             psu=selected_products['psu'],
                             case=selected_products['case'],
                             storage=selected_products['storage'],
                             os=selected_products['os'],
                             cpucooler=selected_products['cpucooler'],
                             )
        return redirect('my_builds')


@method_decorator(login_required, name='dispatch')
class MyBuilds(View):
    def get(self, request):
        builds = Build.objects.filter(author=request.user)
        builds_with_prices = []

        for build in builds:
            # Список всех компонент сборки
            components = [
                build.cpu, build.motherboard, build.ram,
                build.gpu, build.psu, build.case,
                build.storage, build.os, build.cpucooler
            ]

            # Суммируем цены всех компонент, если они существуют
            total_price = sum(component.product.price for component in components if component)

            # Добавляем сборку и её стоимость в список
            builds_with_prices.append({
                'build': build,
                'total_price': total_price
            })

        # Передаём в шаблон список сборок и их стоимость
        return render(request, 'configurator/my_build.html', context={'builds_with_prices': builds_with_prices})


class EditProducts(View):
    def get(self, request):
        return render(request, 'configurator/edit_products.html')

class AddProduct(View):
    def get(self, request, product_category):
        form_classes = {
            'cpu': AddCPUForm,
            'gpu': AddGPUForm,
            'case': AddCaseForm,
            'ram': AddRAMForm,
            'psu': AddPSUForm,
            'cpucooler': AddCPUCoolerForm,
        }

        form = form_classes.get(product_category, lambda: None)()

        return render(request, 'configurator/add_product.html', context={'form': form})


    def post(self, request, product_category):
        form_classes = {
            'cpu': AddCPUForm,
            'gpu': AddGPUForm,
            'case': AddCaseForm,
            'ram': AddRAMForm,
            'psu': AddPSUForm,
            'cpucooler': AddCPUCoolerForm,
        }

        # Получаем класс формы из словаря или None
        form_class = form_classes.get(product_category)

        if not form_class:
            messages.error(request, 'Неверная категория продукта.')
            return redirect('edit_products')

        # Инициализируем форму
        form = form_class(request.POST, request.FILES or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно добавлен.')
            return redirect('edit_products')
        else:
            print(form.errors)
            messages.error(request, 'Произошла ошибка добавления.')
            return redirect('edit_products')


def delete_build(request, build_id):
    build = get_object_or_404(Build, id=build_id, author=request.user)
    build.delete()
    return redirect('my_builds')


def selected_products_from_session(request):
    # Сопоставление категорий с их моделями
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

    # Получение выбранных продуктов из сессии
    session_products = request.session.get('selected_products', {})
    selected_products = {}

    for category, model in model_map.items():
        product_id = session_products.get(category)
        selected_products[category] = model.objects.get(id=product_id) if product_id else None

    return selected_products


