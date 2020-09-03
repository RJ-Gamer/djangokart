from django.contrib import admin
from .models import Order, OrderLine


# Register your models here.
class OrderLineInline(admin.TabularInline):
    model = OrderLine
    raw_id_fields = ('product', )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'status',
    )
    list_filter = (
        'status', 'shipping_country', 'created',
    )
    list_editable = (
        'status',
    )
    inlines = (OrderLineInline, )
    fieldsets = (
        (None, {'fields': ('user', 'status')}),
        (
            'Billing Info',
            {
                'fields': (
                    'billing_name',
                    'billing_address1',
                    'billing_address2',
                    'billing_zip_code',
                    'billing_city',
                    'billing_state',
                    'billing_country'
                )
            },
        ),
        (
            'Shipping Info',
            {
                'fields': (
                    'shipping_name',
                    'shipping_address1',
                    'shipping_address2',
                    'shipping_zip_code',
                    'shipping_city',
                    'shipping_state',
                    'shipping_country',
                )
            },
        ),
    )
@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = (
        'order', 'product', 'status'
    )
