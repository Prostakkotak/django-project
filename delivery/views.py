from django.shortcuts import render, get_object_or_404
from .models import Vehisle, DeliveryClass, News, QuickQuote
from .forms import QuickQuoteForm
from .filters import VehisleFilter
from django.urls import reverse
from django.core.paginator import Paginator


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

    news_per_page = request.GET.get('news_per_page')

    news_list = News.objects.all()

    try:
        paginator = Paginator(news_list, news_per_page)
    except TypeError:
        paginator = Paginator(news_list, 10)
        news_per_page = 10

    important_news_list = News.objects.filter(important_status=True)

    page_num = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    penultimate_page = page_obj.paginator.num_pages - 1

    return render(request, 'delivery/news.html', context={
        'page_obj': page_obj,
        'important_news_list': important_news_list,
        'penultimate_page': penultimate_page,
        'news_per_page': news_per_page
    })


def vehisles(request):
    
    filters = VehisleFilter(request.GET, queryset=Vehisle.objects.all())

    vehisles_per_page = request.GET.get('vehisles_per_page')

    try:
        paginator = Paginator(filters.qs, vehisles_per_page)
    except TypeError:
        paginator = Paginator(filters.qs, 10)
        vehisles_per_page = 10

    page_num = request.GET.get('page') 

    try:
        page_obj = paginator.get_page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    penultimate_page = page_obj.paginator.num_pages - 1

    return render(request, 'delivery/vehisles.html', context={
        'page_obj': page_obj,
        'penultimate_page': penultimate_page,
        'vehisles_per_page': vehisles_per_page,
        'filters': filters,
    })
