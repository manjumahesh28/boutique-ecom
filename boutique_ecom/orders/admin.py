from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
         list_display = ['id', 'user', 'total', 'status', 'created_at']  # Fixed: 'created_at'
         list_filter = ['status', 'created_at']  # Fixed: 'created_at'
         search_fields = ['user__username', 'id']
         readonly_fields = ['created_at', 'updated_at']  # Prevent editing timestamps
         date_hierarchy = 'created_at'  # Quick date navigation

         def get_readonly_fields(self, request, obj=None):
             if obj:  # Edit mode: Make total readonly too
                 return self.readonly_fields + ['total']
             return self.readonly_fields

     
@admin.register(OrderItem)  # Enhanced: Use @register for consistency
class OrderItemAdmin(admin.ModelAdmin):
         list_display = ['order', 'product', 'quantity', 'price', 'subtotal']
         list_filter = ['order__status']
         search_fields = ['product__name', 'order__id']

         def subtotal(self, obj):
             return f"${obj.subtotal:,.2f}"  # Formatted display
         subtotal.short_description = 'Subtotal'
     