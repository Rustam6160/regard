from django.db import models
from accounts.models import CustomUser
from configurator.models import Product




class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField(Product, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity


class Favorite(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='favorites')
    products = models.ManyToManyField(Product)