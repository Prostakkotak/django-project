from django.shortcuts import render, get_object_or_404
from .models import Vehisle, DeliveryClass, News, QuickQuote
from .forms import QuickQuoteForm
from .filters import VehisleFilter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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

    if (method == 'ground'):  # Method это метод доставки, для каждого типа доставки своя страница и шаблон
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

    # Функция берет данные из GET запроса и возвращает список для сортировки
    def ordering(datatype):

        ordering_obj = {
            'pub_date': 'pub date',
            'title': 'title',
            'short_description': 'description',
        }

        if datatype == 'obj':
            return ordering_obj
        elif datatype == 'keys':
            ordering_keys = list(ordering_obj.keys())

            # Проверка GET данных из чекбоксов в форме сортировки
            for i in range(len(ordering_keys)):
                if request.GET.get('ordering__' + ordering_keys[i]) == 'on':
                    ordering_keys[i] = '-' + ordering_keys[i]
                else:
                    pass

            return ordering_keys

    if request.GET.get('ordering') == 'off':
        news_list = News.objects.all().order_by('-pub_date')
    else:
        news_list = News.objects.all().order_by(*ordering('keys'))

    news_per_page = request.GET.get('news_per_page')

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
        'news_per_page': news_per_page,
        'ordering_obj': ordering('obj')
    })


def vehisles(request):

    vehisles_per_page = request.GET.get('vehisles_per_page')

    if request.GET.get('filters') == 'off':
        vehisles_list = Vehisle.objects.all()

        # Здесь фильтры нужны только для вывода формы на страницу
        filters = VehisleFilter(request.GET, queryset=Vehisle.objects.all())

        try:
            paginator = Paginator(vehisles_list, vehisles_per_page)
        except TypeError:
            paginator = Paginator(vehisles_list, 10)
            vehisles_per_page = 10
    else:
        filters = VehisleFilter(request.GET, queryset=Vehisle.objects.all())

        try:
            paginator = Paginator(filters.qs, vehisles_per_page)
        except TypeError:
            paginator = Paginator(filters.qs, 10)
            vehisles_per_page = 10

        # Если по итогам фильтрации ничего не нашлось, то будет создана переменная с ошибкой
        if len(filters.qs) == 0:
            filter_res_error = 'Nothing found by the specified parameters'
        else:
            filter_res_count = len(filters.qs)

    page_num = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    penultimate_page = page_obj.paginator.num_pages - 1

    context = {
        'page_obj': page_obj,
        'penultimate_page': penultimate_page,
        'vehisles_per_page': vehisles_per_page,
        'filters': filters,
    }

    if request.GET.get('filters') != 'off':
        try:  # Проверка на существование переменных с результатами фильтрации
            context['filter_res_count'] = filter_res_count
        except UnboundLocalError:  # Если ничего нет, то в шаблон передается ошибка вместо результатов
            context['filter_res_error'] = filter_res_error

    return render(request, 'delivery/vehisles.html', context)