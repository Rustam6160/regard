from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductView.as_view(), name='products'),
    path('favorites/', favorites_view, name='favorites_view'),
    path('favorites/add/<int:product_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:product_id>/', remove_from_favorites, name='remove_from_favorites'),

    path('cart/', cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),

    path('product_type/<str:product_type>', CategoryView.as_view(), name='product_type'),
    path('product_features/<str:product_type>/<int:product_id>', ProductFeaturesView.as_view(), name='product_features'),
]