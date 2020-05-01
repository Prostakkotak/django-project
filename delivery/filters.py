import django_filters
from .models import Vehisle
from django.db import models
from django import forms

class VehisleFilter(django_filters.FilterSet) :
    class Meta :
        model = Vehisle
        fields = [
            'can_be_booked',
            'delivery_method',
            'status',
        ]
        filter_overrides = {
            models.BooleanField: {
                'filter_class': django_filters.BooleanFilter,
                'extra': lambda f: {
                    'widget': forms.CheckboxInput,
                },
            },
            models.IntegerField: {
                'filter_class': django_filters.RangeFilter,
                'extra': lambda f: {
                    'widget': forms.NumberInput(),
                }
            }
        }