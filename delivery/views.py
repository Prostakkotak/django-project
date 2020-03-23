from django.shortcuts import render
from .models import Vehisle, DeliveryClass, News

def index(request) :
    vehisle_list = Vehisle.objects.all()
    delivery_class_list = DeliveryClass.objects.all()
    news_list = News.objects.all()[:3]

    return render(request, 'delivery/index.html', context={
        'vehisle_list': vehisle_list,
        'delivery_class_list': delivery_class_list,
        'news_list': news_list,
    })

def delivery_method(request, method) :

    vehisle_list = Vehisle.objects.all()
    delivery_class_list = DeliveryClass.objects.all()

    if (method == 'ground') :
        htmlPath = 'delivery/ground-delivery.html'
    elif (method == 'air') :
        htmlPath = 'delivery/air-delivery.html'
    elif (method == 'sea') :
        htmlPath = 'delivery/sea-delivery.html'

    return render(request, htmlPath, context={
        'vehisle_list': vehisle_list,
        'delivery_class_list': delivery_class_list,
    })