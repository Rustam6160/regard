from django.urls import path
from .views import *

urlpatterns = [
    # Маршрут для основного представления
    path('configurator/<str:selected_product_category>/<int:selected_product_id>/',
         ConfiguratorView.as_view(), name='configurator'),

    path('save_build/', SaveMyBuild.as_view(), name='save_build'),
    path('my_builds/', MyBuilds.as_view(), name='my_builds'),
    path('delete_build/<int:build_id>/', delete_build, name='delete_build'),
    path('edit_products/', EditProducts.as_view(), name='edit_products'),
    path('add_product/<str:product_category>', AddProduct.as_view(), name='add_product'),
]
