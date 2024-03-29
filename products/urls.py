from django.urls import path, include
from .views import (
    product_create_view,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view,
)

app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view),
    path('<int:id>', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
]
