import django_filters
from .models import Vehisle
from django.db import models
from django import forms

class VehisleFilter(django_filters.FilterSet) :
    class Meta :
        model = Vehisle
        fields = [
            'delivery_method',
            'status',
            'price_per_use',
            'price_per_km',
            'maximum_load',
            'cargo_volume'
        ]