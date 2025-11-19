from django.db import models
from django.conf import settings
from cart.models import CartItem  # Link to cart

class Order(models.Model):
         STATUS_CHOICES = [
             ('pending', 'Pending'),
             ('paid', 'Paid'),
             ('shipped', 'Shipped'),
             ('delivered', 'Delivered'),
         ]
         user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
         created_at = models.DateTimeField(auto_now_add=True)
         updated_at = models.DateTimeField(auto_now=True)
         status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
         total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

         class Meta:
             ordering = ['-created_at']

         def __str__(self):
             return f"Order {self.id} - {self.user.username}"

class OrderItem(models.Model):
         order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
         product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
         quantity = models.PositiveIntegerField(default=1)
         price = models.DecimalField(max_digits=10, decimal_places=2)  # Price at time of order

         def __str__(self):
             return f"{self.quantity} x {self.product.name}"

         @property
         def subtotal(self):
             return self.quantity * self.price
     