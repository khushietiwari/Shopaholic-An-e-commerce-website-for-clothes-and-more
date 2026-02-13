from django.urls import path
from .views import dashboard, update_stock, admin_login,admin_products,add_product,edit_product,delete_product

app_name = 'adminapp'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', admin_login, name='admin_login'),
    path('update-stock/<int:product_id>/', update_stock, name='update_stock'),
    path('products/', admin_products, name='admin_products'),
    path('products/add/', add_product, name='add_product'),
    path('products/edit/<int:product_id>/',edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', delete_product, name='delete_product'),

]
