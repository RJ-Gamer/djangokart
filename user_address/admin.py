from django.contrib import admin
from .models import Address

# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'zip_code', 'city', 'state', 'country'
    )
    list_filter = (
        'city', 'state', 'country'
    )
    search_fields = (
        'address1', 'address2', 'city'
    )
    
