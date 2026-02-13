from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Product, Cart, Order


# HOME
def home(request):
    speak = False

    if request.session.get('just_logged_in'):
        speak = True
        del request.session['just_logged_in']

    products = Product.objects.all()

    return render(request, 'shop/home.html', {
        'products': products,
        'speak': speak
    })




# ADD TO CART
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('shop:view_cart')


# VIEW CART
@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)

    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.quantity

    speak = False

    if request.session.get('just_logged_in'):
        speak = True
        del request.session['just_logged_in']

    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'speak': speak   # ✅ CRITICAL
    })



# REMOVE FROM CART (ONLY ONCE)
@login_required
def remove_from_cart(request, cart_id):
    Cart.objects.filter(id=cart_id, user=request.user).delete()
    return redirect('shop:view_cart')


# COLLECTION + CATEGORY SEARCH
def collection(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query)
        )
    else:
        products = Product.objects.all()

    return render(request, 'shop/collection.html', {
        'products': products,
        'query': query
    })


# SEARCH PAGE
def search(request):
    query = request.GET.get('q')
    products = []

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query)
        )

    return render(request, 'shop/search.html', {
        'products': products,
        'query': query
    })


# PRODUCT DETAIL
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {
        'product': product
    })


# ABOUT & CONTACT
def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


# CHECKOUT → CREATE ORDERS
@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    if request.method == 'POST':
        for item in cart_items:
            Order.objects.create(
                user=request.user,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        cart_items.delete()
        return redirect('shop:my_orders')

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })


# MY ORDERS (REAL ORDERS)
@login_required
def my_orders(request):
    orders = Order.objects.filter(
        user=request.user
    ).order_by('-ordered_at')

    return render(request, 'shop/my_orders.html', {
        'orders': orders
    })
@login_required
def increase_quantity(request, cart_id):
    item = Cart.objects.get(id=cart_id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('shop:view_cart')


@login_required
def decrease_quantity(request, cart_id):
    item = Cart.objects.get(id=cart_id, user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()   # remove if quantity becomes 0

    return redirect('shop:view_cart')

