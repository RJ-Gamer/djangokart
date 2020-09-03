from django.contrib import admin
from .models import Basket, BasketLine


# Register your models here.
class BasketLineInline(admin.TabularInline):
    model = BasketLine
    raw_id_fields = ('product', )

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'status', 'count'
    )
    list_editable = (
        'status',
    )
    list_filter = (
        'status',
    )
    inlines = (BasketLineInline,)

@admin.register(BasketLine)
class BasketLineAdmin(admin.ModelAdmin):
    list_display = (
        'basket', 'product', 'quantity',
    )
