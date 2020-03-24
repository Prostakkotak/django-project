from django.db import models
from tinymce.models import HTMLField

class DeliveryClass(models.Model) :
    delivery_class = models.CharField(max_length=50, default='econom')
    price_multiplier = models.FloatField(default=1)

    class Meta :
        verbose_name = 'Delivery class'
        verbose_name_plural = 'Delivery classes'

    def __str__(self) :
        return self.delivery_class + ' ' + str(self.price_multiplier) + 'x'

class Vehisle(models.Model) :
    model = models.CharField(max_length=50, help_text='Enter here the model of vehisle', default='unknown')
    kind_of_vehisle = models.CharField(max_length=70, help_text='Kind of vehisle(helicopter, truck, ship and others)', default='truck')
    photo = models.ImageField(default='photo')

    can_be_booked = models.BooleanField(default=True)

    DELIVERY_METHODS = (
        ('ground', 'Ground'),
        ('air', 'Air'),
        ('sea', 'Sea'),
    )

    STATUS_VARIABLES = (
        ('a', 'Available'),
        ('u', 'Unavailable'),
        ('m', 'Maintenance'),
        ('b', 'Booked'),
    )

    delivery_method = models.CharField(max_length=6, choices=DELIVERY_METHODS, blank=True, default='g') 
    status = models.CharField(max_length=1, choices=STATUS_VARIABLES, blank=True, default='m')

    price_per_use = models.IntegerField(default=100)
    price_per_km = models.IntegerField(default=20)
    km_per_day = models.PositiveSmallIntegerField(help_text='How much transport does it cover kilometers per day', default=50)

    maximum_load = models.IntegerField(help_text='Enter maximum load in kilogramms', default=1000)
    cargo_volume = models.IntegerField(help_text='Enter cargo volume in cubic meter', default=10)

    class Meta :
        ordering = ['price_per_use', 'maximum_load', 'cargo_volume']

    def __str__(self) :
        return (self.model + ' ' + self.kind_of_vehisle)

class News(models.Model) :
    title = models.CharField(max_length=50)
    title_image = models.ImageField(default='none')
    short_description = models.CharField(max_length=200, default='Desctiption')
    content = HTMLField()

    class Meta :
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self) :
        return self.title

class QuickQuote(models.Model):
    name = models.CharField(max_length=50, default='Your Name')
    subject = models.CharField(max_length=50, default='Subject')
    email = models.EmailField(default='Your@EmailAdress')
    phone = models.IntegerField(default=0)
    service = models.CharField(max_length=50, default='Service')
    message = models.CharField(max_length=200, default='Message')