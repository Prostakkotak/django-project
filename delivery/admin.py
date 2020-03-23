from django.contrib import admin
from .models import Vehisle, DeliveryClass, News

@admin.register(Vehisle)
class VehisleAdmin(admin.ModelAdmin) :
    fields = [
        ('model', 'kind_of_vehisle'),
        'photo',
        ('delivery_method','status'), 'can_be_booked',
        'price_per_use', 'price_per_km', 'km_per_day',
        ('maximum_load', 'cargo_volume')
        ]

    list_filter = ('price_per_use', 'maximum_load', 'cargo_volume')
    list_display = ('model', 'maximum_load', 'cargo_volume')

@admin.register(DeliveryClass)
class DeliveryClassAdmin(admin.ModelAdmin) :
    list_display = ('delivery_class', 'price_multiplier')

admin.site.register(News)