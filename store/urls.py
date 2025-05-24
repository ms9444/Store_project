from django.urls import path
from .views import ProductList, CartDetail

urlpatterns = [
    path('products/', ProductList.as_view(), name='product_list'),
    path('cart/', CartDetail.as_view(), name='cart_detail'),
]