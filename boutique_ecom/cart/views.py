from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart, CartItem
from django.contrib import messages

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if created:
        messages.info(request, 'Your cart has been created.')

    items = cart.items.all()   
    total = sum(item.product.price * item.quantity for item in items)

    context = {
        'cart': cart,
        'items': items,
        'total': total,
    }
    return render(request, 'cart/detail.html', context)

@login_required
def add_to_cart(request, product_id):
         product = get_object_or_404(Product, id=product_id)
         cart, created = Cart.objects.get_or_create(user=request.user)
         
         # Get or create CartItem
         cart_item, item_created = CartItem.objects.get_or_create(
             cart=cart,
             product=product,
             defaults={'quantity': 1}  # If new, set quantity=1
         )
         
         if not item_created:
             cart_item.quantity += 1  # Increment if exists
             cart_item.save()
         
         messages.success(request, f'{product.name} added to cart!')
         return redirect('cart_detail')

@login_required
def remove_from_cart(request, item_id):
         cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
         product_name = cart_item.product.name
         cart_item.delete()
         messages.success(request, f'{product_name} removed from cart.')
         return redirect('cart_detail')
