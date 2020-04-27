from django.db import models
from tinymce.models import HTMLField
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_delete

class DeliveryClass(models.Model):
    delivery_class = models.CharField(max_length=50, default='econom')
    price_multiplier = models.FloatField(default=1)

    class Meta:
        verbose_name = 'Delivery class'
        verbose_name_plural = 'Delivery classes'

    def __str__(self):
        return self.delivery_class + ' ' + str(self.price_multiplier) + 'x'


class Vehisle(models.Model):
    model = models.CharField(
        max_length=50, help_text='Enter here the model of vehisle', default='unknown')
    kind_of_vehisle = models.CharField(
        max_length=70, help_text='Kind of vehisle(helicopter, truck, ship and others)', default='truck')
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

    delivery_method = models.CharField(
        max_length=6, choices=DELIVERY_METHODS, blank=True, default='g')
    status = models.CharField(
        max_length=1, choices=STATUS_VARIABLES, blank=True, default='m')

    price_per_use = models.IntegerField(default=100)
    price_per_km = models.IntegerField(default=20)
    km_per_day = models.PositiveSmallIntegerField(
        help_text='How much transport does it cover kilometers per day', default=50)

    maximum_load = models.IntegerField(
        help_text='Enter maximum load in kilogramms', default=1000)
    cargo_volume = models.IntegerField(
        help_text='Enter cargo volume in cubic meter', default=10)

    class Meta:
        ordering = ['price_per_use', 'maximum_load', 'cargo_volume']

    def __str__(self):
        return (self.model + ' ' + self.kind_of_vehisle)


class NewsTag(models.Model):
    tagname = models.CharField(max_length=20)

    def __str__(self):
        return self.tagname


class NewsComment(models.Model):
    message = models.TextField()
    news = models.ForeignKey(
        'News', on_delete=models.CASCADE, related_name='news_comment', null=True, blank=True)
    pub_date = models.DateTimeField(default=datetime.now(), editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    answer = models.ForeignKey('NewsComment', related_name='comment_answer', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-pub_date', ]


class News(models.Model):
    title = models.CharField(max_length=50)
    title_image = models.ImageField(default='none')
    short_description = models.CharField(max_length=200, default='Description')
    content = HTMLField()
    pub_date = models.DateTimeField(default=datetime.now(), blank=True)
    important_status = models.BooleanField(
        default=False, help_text='Are this news important or not')
    views = models.IntegerField(default=0, editable=False)
    tags = models.ManyToManyField(NewsTag)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = ' News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class ProposedNews(models.Model):
    title = models.CharField(max_length=50)
    title_image = models.ImageField(default='none')
    short_description = models.CharField(max_length=200, default='Description')
    content = HTMLField()
    pub_date = models.DateTimeField(default=datetime.now(), blank=True)
    important_status = models.BooleanField(
        default=False, help_text='Are this news important or not')
    views = models.IntegerField(default=0, editable=False)
    tags = models.ManyToManyField(NewsTag)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Proposed news'
        verbose_name_plural = 'Proposed news'

    def __str__(self):
        return self.title


class QuickQuote(models.Model):
    name = models.CharField(max_length=50, default='Your Name')
    subject = models.CharField(max_length=50, default='Subject')
    email = models.EmailField(default='Your@EmailAdress')
    phone = models.IntegerField(default=0)
    service = models.CharField(max_length=50, default='Service')
    message = models.CharField(max_length=200, default='Message')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
