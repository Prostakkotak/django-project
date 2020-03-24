from django.shortcuts import render, get_object_or_404
from .models import Vehisle, DeliveryClass, News, QuickQuote
from .forms import QuickQuoteForm


def index(request):
    vehisle_list = Vehisle.objects.all()[:5]
    delivery_class_list = DeliveryClass.objects.all()
    news_list = News.objects.all()[:3]

    if request.method == 'POST':
        quick_quote_form = QuickQuoteForm(request.POST)

        if quick_quote_form.is_valid():
            quick_quote_form.save()
            quick_quote_form = QuickQuoteForm()
    else:
        quick_quote_form = QuickQuoteForm()

    return render(request, 'delivery/index.html', context={
        'vehisle_list': vehisle_list,
        'delivery_class_list': delivery_class_list,
        'news_list': news_list,
        'quick_quote_form': quick_quote_form,
    })


def delivery_method(request, method):

    vehisle_list = Vehisle.objects.all()
    delivery_class_list = DeliveryClass.objects.all()

    if (method == 'ground'):
        htmlPath = 'delivery/ground-delivery.html'
    elif (method == 'air'):
        htmlPath = 'delivery/air-delivery.html'
    elif (method == 'sea'):
        htmlPath = 'delivery/sea-delivery.html'

    return render(request, htmlPath, context={
        'vehisle_list': vehisle_list,
        'delivery_class_list': delivery_class_list,
    })


def news_single(request, pk):
    news_content = get_object_or_404(News, pk=pk)
    return render(request, 'delivery/news-single.html', context={
        'news_content': news_content,
    })


def news(request):
    news_list = News.objects.all()
    return render(request, 'delivery/news.html', context={
        'news_list': news_list
    })
