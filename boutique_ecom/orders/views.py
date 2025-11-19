from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order, OrderItem
import stripe
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages
from django.db import transaction
from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
@transaction.atomic
def create_order(request):
    if request.method == 'POST':
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        items = cart.items.all() if hasattr(cart, 'items') else cart.cartitem_set.all()
        if not items.exists():
            messages.error(request, "Your cart is empty.")
            return redirect('cart_detail')

        order = Order.objects.create(user=request.user, total=cart.total)

        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        items.delete()

        
        return redirect('orders:order_detail', order_id=order.id)

    return redirect('cart_detail')

@csrf_exempt
def stripe_webhook(request):
         payload = request.body
         sig_header = request.META['HTTP_STRIPE_SIGNATURE']
         try:
             event = stripe.Webhook.construct_event(
                 payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
             )
             print(f"✅ Webhook received: {event['type']} for order {event['data']['object'].get('metadata', {}).get('order_id', 'N/A')}")  # Debug log
         except ValueError as e:
             print(f"❌ Invalid payload: {e}")
             return JsonResponse({'error': 'Invalid payload'}, status=400)
         except stripe.error.SignatureVerificationError as e:
             print(f"❌ Invalid signature: {e}")
             return JsonResponse({'error': 'Invalid signature'}, status=400)

         if event['type'] == 'checkout.session.completed':
             session = event['data']['object']
             order_id = int(session['metadata']['order_id'])
             order = Order.objects.get(id=order_id)
             order.status = 'paid'
             order.save()
             print(f"💰 Order {order_id} marked as paid!")

         return JsonResponse({'status': 'success'}, status=200)
     
@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def order_list(request):
         orders = Order.objects.filter(user=request.user)
         return render(request, 'orders/list.html', {'orders': orders})