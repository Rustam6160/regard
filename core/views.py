from django.http import JsonResponse, HttpResponse
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from configurator.models import *


class ProductView(View):
    def get(self, request):
        pro = Product.objects.all()


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

