from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

from shop.models import Product, Order,Category


def is_admin(user):
    return user.is_superuser


@login_required
@user_passes_test(is_admin)
def dashboard(request):
    users = User.objects.all()
    products = Product.objects.all()
    orders = Order.objects.select_related('user', 'product').order_by('-ordered_at')

    total_revenue = sum(
        order.price * order.quantity
        for order in orders
    )

    return render(request, 'adminapp/dashboard.html', {
        'users': users,
        'products': products,
        'orders': orders,
        'total_revenue': total_revenue,
    })


@user_passes_test(is_admin)
def update_stock(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        new_stock = request.POST.get('stock')

        if new_stock is not None:
            product.stock = int(new_stock)
            product.save()

    return redirect('adminapp:dashboard')


def admin_login(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('adminapp:dashboard')
        else:
            return redirect('shop:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('adminapp:dashboard')
        else:
            messages.error(request, 'Invalid admin credentials')

    return render(request, 'adminapp/admin_login.html')
@login_required
@user_passes_test(is_admin)
def admin_products(request):
    products = Product.objects.all()
    return render(request, 'adminapp/products/product_list.html', {
        'products': products
    })

@login_required
@user_passes_test(is_admin)
def add_product(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        Product.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            stock=request.POST.get('stock'),
            description=request.POST.get('description'),
            category_id=request.POST.get('category'),
            image=request.FILES.get('image')
        )
        return redirect('adminapp:admin_products')

    return render(request, 'adminapp/products/product_form.html', {
        'categories': categories,
        'title': 'Add Product'
    })


@login_required
@user_passes_test(is_admin)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        product.description = request.POST.get('description')
        product.category_id = request.POST.get('category')

        if request.FILES.get('image'):
            product.image = request.FILES.get('image')

        product.save()
        return redirect('adminapp:admin_products')

    return render(request, 'adminapp/products/product_form.html', {
        'product': product,
        'categories': categories,
        'title': 'Edit Product'
    })


@login_required
@user_passes_test(is_admin)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('adminapp:admin_products')

