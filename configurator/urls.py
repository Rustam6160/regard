from django.urls import path
from .views import *

urlpatterns = [
    # Маршрут для основного представления
    path('configurator/<str:selected_product_category>/<int:selected_product_id>/',
         ConfiguratorView.as_view(), name='configurator'),

    path('', ProductView.as_view(), name='products'),
]