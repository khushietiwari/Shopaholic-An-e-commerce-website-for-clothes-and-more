from django.urls import path
from .views import (
    home,
    collection,
    about,
    contact,
    add_to_cart,
    view_cart,
    remove_from_cart,
    product_detail,
    search,
    checkout,
    my_orders,
)

app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('collection/', collection, name='collection'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('my-orders/', my_orders, name='my_orders'),


    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name='checkout'),
    path('search/', search, name='search'),
    path('remove/<int:cart_id>/', remove_from_cart, name='remove_from_cart'),  # ✅ REQUIRED
]
