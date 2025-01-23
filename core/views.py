from django.http import JsonResponse, HttpResponse
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from configurator.models import *
from django.db.models import Field


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


class CategoryView(View):
    def get(self, request, product_type):
        categories = {
            "cpu": CPU,
            "motherboard": Motherboard,
            "ram": RAM,
            "gpu": GPU,
            "psu": PSU,
            "case": Case,
            "storage": Storage,
            "os": OS,
            "cpucooler": CPUCooler,
        }
        products = categories.get(product_type).objects.all()
        return render(request, 'core/product_list.html', context={'products': products})


class ProductFeaturesView(View):
    def get(self, request, product_type, product_id):
        categories = {
            "cpu": CPU,
            "motherboard": Motherboard,
            "ram": RAM,
            "gpu": GPU,
            "psu": PSU,
            "case": Case,
            "storage": Storage,
            "os": OS,
            "cpucooler": CPUCooler,
        }
        product = categories.get(product_type).objects.get(id=product_id)
        instance = categories.get(product_type).objects.get(id=product_id)  # Получаем экземпляр модели
        field_values = {field.verbose_name: getattr(instance, field.name) for field in instance._meta.get_fields() if
                        isinstance(field, Field)}
        field_values['price'] = instance.product.price
        print(field_values)

        return render(request, 'core/product_features.html', context={'product': product, 'field_values': field_values})


@login_required
def cart_view(request):
    cart = request.user.cart
    items = cart.cartitem_set.all()
    total_price = sum(item.get_total_price() for item in items)
    return render(request, 'core/cart.html', {'cart': cart, 'items': items, 'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    cart = request.user.cart
    product = get_object_or_404(Product, id=product_id)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return HttpResponse(status=204)

@login_required
def remove_from_cart(request, product_id):
    cart = request.user.cart
    product = get_object_or_404(Product, id=product_id)
    CartItem.objects.filter(cart=cart, product=product).delete()
    return redirect('cart_view')


@login_required
def favorites_view(request):
    favorites = request.user.favorites
    return render(request, 'core/favorites.html', {'favorites': favorites.products.all()})

@login_required
def add_to_favorites(request, product_id):
    favorites = request.user.favorites
    product = get_object_or_404(Product, id=product_id)
    favorites.products.add(product)
    return HttpResponse(status=204)

@login_required
def remove_from_favorites(request, product_id):
    favorites = request.user.favorites
    product = get_object_or_404(Product, id=product_id)
    favorites.products.remove(product)
    return redirect('favorites_view')

