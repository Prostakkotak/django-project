from django.shortcuts import render, get_object_or_404, Http404, redirect
from .models import Vehisle, DeliveryClass, News, QuickQuote, NewsTag, NewsComment, ProposedNews
from .forms import QuickQuoteForm, NewsCommentForm, NewsProposeForm, CreateNewsForm, CreateDeliveryClassForm, CreateVehisleForm
from .filters import VehisleFilter
from .ordering import ordering
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F, Q
from django.utils import timezone


def index(request):
    vehisle_list = Vehisle.objects.all()[:5]
    delivery_class_list = DeliveryClass.objects.all()
    news_list = News.objects.all()[:3]

    quick_quote_form = QuickQuoteForm(data=request.POST or None)

    if request.method == 'POST' and quick_quote_form.is_valid():
        if request.user.has_perm('delivery.add_quickquote'):
            quick_quote_form = QuickQuoteForm(data=request.POST)
            created_quote = quick_quote_form.save()
            created_quote.user = request.user
            created_quote.save()

            '''
            Редирект здесь нужен для сброса типа запроса,
            без этого при каждом обновлении страницы тип запроса будет POST,
            что приведет к отправке формы при каждом обновлении
            '''
            return redirect('index')
        else:
            return redirect('index')
    elif request.method == 'POST' and not quick_quote_form.is_valid():
        return redirect('index')

    return render(request, 'delivery/index.html', context={
        'vehisle_list': vehisle_list,
        'delivery_class_list': delivery_class_list,
        'news_list': news_list,
        'quick_quote_form': quick_quote_form,
    })


def return_button(request, path):
    return redirect(path)


def control(request):
    context = {
        'proposed_news_count': ProposedNews.objects.all().count(),
        'proposed_news_list': ProposedNews.objects.all(),
        'quick_quote_count': QuickQuote.objects.all().count(),
        'quick_quote_list': QuickQuote.objects.all(),
        'news_count': News.objects.all().count(),
        'news_list': News.objects.all(),
        'vehisles_count': Vehisle.objects.all().count(),
        'vehisles_list': Vehisle.objects.all(),
        'delivery_class_count': DeliveryClass.objects.all().count(),
        'delivery_class_list': DeliveryClass.objects.all(),
    }

    return render(request, 'delivery/control-panel.html', context)


def registration(request):
    form = UserCreationForm(data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        u_name = form.cleaned_data.get('username')
        u_pass = form.cleaned_data.get('password2')

        form.save()

        user = authenticate(
            username=u_name,
            password=u_pass
        )

        # Добавляем нового пользователя в стандартную группу users
        my_group = Group.objects.get(name='users')
        my_group.user_set.add(user)

        login(request, user)  # Логиним пользователя после успешной регистрации

        return redirect('index')

    return render(request, 'registration/registration.html', context={
        'form': form,
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
    context = {}

    news_content = get_object_or_404(News, pk=pk)

    # инкрементируем счётчик просмотров и обновляем поле в базе данных
    News.objects.filter(id=pk).update(views=F('views')+1)

    # Сбор тегов для поиска похожих статей
    tags_get = list(news_content.tags.all())
    news_list = News.objects.exclude(id=pk)

    news_comment_form = NewsCommentForm(data=request.POST or None)

    for t in tags_get:
        news_list = news_list.filter(tags__tagname__contains=t)

    if request.method == 'POST' and news_comment_form.is_valid():
        news_comment = news_comment_form.save(commit=False)
        news_comment.user = request.user

        if request.POST.get('answer'):
            news_comment.answer = get_object_or_404(
                NewsComment, pk=int(request.POST.get('answer')))

        news_comment.news = news_content

        news_comment.save()

        return redirect('news_single', pk=pk)

    news_list = news_list[:4]

    if len(news_list) == 0:
        context['similar_news_error'] = 'There is nothing like that'

    context.update({
        'news_content': news_content,
        'similar_news_list': news_list,
        'similar_news_tags': tags_get,
        'news_comment_form': news_comment_form,
    })

    return render(request, 'delivery/news-single.html', context)


def offer_news(request):
    context = {}

    form = NewsProposeForm(data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form = NewsProposeForm(request.POST, request.FILES)
        proposed_news = form.save()
        proposed_news.user = request.user
        proposed_news.save()

        return redirect('news')

    context.update({
        'form': form,
    })

    return render(request, 'delivery/create-model.html', context)


def proposed_news_demo(request, pk):
    news_content = get_object_or_404(ProposedNews, pk=pk)

    context = {
        'news_content': news_content,
    }

    return render(request, 'delivery/propose-news-demo.html', context)


def confirmed_proposed_news(request, pk):
    if request.user.has_perm('delivery.add_news'):
        proposed_news = get_object_or_404(ProposedNews, pk=pk)

        confirmed_news = News(
            user=proposed_news.user,
            title=proposed_news.title,
            title_image=proposed_news.title_image,
            short_description=proposed_news.short_description,
            content=proposed_news.content,
            important_status=proposed_news.important_status,
        )

        confirmed_news.save()

        for tag in proposed_news.tags.all():
            confirmed_news.tags.add(tag)

        proposed_news.delete()

        return redirect('control')


def delete_proposed_news(request, pk):
    proposed_news = ProposedNews.objects.get(pk=pk)

    if request.user.has_perm('delivery.delete_proposednews') or request.user.pk == proposed_news.user.pk:
        proposed_news.delete()

    return redirect('control')


def create_news(request):

    if request.user.has_perm('delivery.add_news'):
        form = CreateNewsForm(data=request.POST or None)

        if request.method == 'POST' and form.is_valid() and request.user.has_perm('delivery.add_news'):
            form = CreateNewsForm(request.POST, request.FILES)
            created_news = form.save()
            created_news.user = request.user
            created_news.save()
            return redirect('control')

        context = {'form': form}

        return render(request, 'delivery/create-model.html', context)

    else:
        return redirect('index')


def change_news(request, pk):
    context = {}

    news = get_object_or_404(News, pk=pk)

    form = CreateNewsForm(data=request.POST or None, instance=news)

    if request.method == 'POST' and form.is_valid():
        form = CreateNewsForm(request.POST, request.FILES, instance=news)
        form.save()
        return redirect('control')

    context['form'] = form

    return render(request, 'delivery/create-model.html', context)


def news_single_delete(request, pk):
    news = News.objects.get(pk=pk)

    if request.user.has_perm('delivery.delete_news') or request.user.pk == news.user.pk:
        news.delete()

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('news')
    else:
        return redirect('news')


def delete_news_comment(request, pk):
    comment = NewsComment.objects.get(pk=pk)

    if request.user.has_perm('delivery.delete_newscomment') or comment.user.pk == request.user.pk:
        comment.delete()

    return_path = request.META.get('HTTP_REFERER', '/')
    return redirect(return_path)


def news(request):

    context = {}

    ordering_obj = {
        'pub_date': 'pub date',
        'title': 'title',
        'short_description': 'description',
        'views': 'views',
    }

    tags_list = NewsTag.objects.all()

    if request.GET.get('ordering_status') == 'on':
        tags_get = []
        news_list = News.objects.all()

        for tag in list(tags_list):
            if request.GET.get('tags__' + tag.tagname) == 'on':
                tags_get.append(tag)

        for t in tags_get:
            news_list = news_list.filter(tags__tagname__contains=t)

        news_list = news_list.order_by(*ordering(request, ordering_obj))
    else:
        news_list = News.objects.filter().order_by('-pub_date')

    news_per_page = request.GET.get('news_per_page')

    try:
        paginator = Paginator(news_list, news_per_page)
    except TypeError:
        paginator = Paginator(news_list, 10)
        news_per_page = 10

    important_news_list = News.objects.filter(
        important_status=True,
        pub_date__range=[  # Выводятся новости только за последние 7 дней
            timezone.now() - timezone.timedelta(days=7), timezone.now() +
            timezone.timedelta(days=1)
        ]
    )

    if len(important_news_list) == 0:
        context['important_news_empty'] = 'Nothing important in last 7 days'

    page_num = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    penultimate_page = page_obj.paginator.num_pages - 1

    context.update({
        'page_obj': page_obj,
        'important_news_list': important_news_list,
        'penultimate_page': penultimate_page,
        'news_per_page': news_per_page,
        'ordering_obj': ordering_obj,
        'tags_list': tags_list,
    })

    return render(request, 'delivery/news.html', context)


def vehisles(request):

    context = {}

    vehisles_per_page = request.GET.get('vehisles_per_page')

    ordering_obj = {
        'price_per_use': 'price per use',
        'price_per_km': 'price per km',
        'km_per_day': 'km per day',
        'maximum_load': 'max load',
        'cargo_volume': 'cargo volume',
    }

    price_per_use_max = 0
    price_per_km_max = 0
    maximum_load_max = 0
    cargo_volume_max = 0

    for item in Vehisle.objects.all():
        if item.price_per_use > price_per_use_max:
            price_per_use_max = item.price_per_use
        if item.price_per_km > price_per_km_max:
            price_per_km_max = item.price_per_km
        if item.maximum_load > maximum_load_max:
            maximum_load_max = item.maximum_load
        if item.cargo_volume > cargo_volume_max:
            cargo_volume_max = item.cargo_volume

    
    context.update({
        'price_per_use_max': price_per_use_max,
        'price_per_km_max': price_per_km_max,
        'maximum_load_max': maximum_load_max,
        'cargo_volume_max': cargo_volume_max,
    })


    if request.GET.get('filters_status') == 'on':
        vehisles_list = Vehisle.objects.filter(
            price_per_use__range=[
                request.GET.get('price_per_use_from'),
                request.GET.get('price_per_use_to')
            ],
            price_per_km__range=[
                request.GET.get('price_per_km_from'),
                request.GET.get('price_per_km_to')
            ],
            maximum_load__range=[
                request.GET.get('maximum_load_from'),
                request.GET.get('maximum_load_to')
            ],
            cargo_volume__range=[
                request.GET.get('cargo_volume_from'),
                request.GET.get('cargo_volume_to')
            ]
        ).order_by(*ordering(request, ordering_obj))

        filters = VehisleFilter(
            request.GET, queryset=vehisles_list
        )

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

    else:
        vehisles_list = Vehisle.objects.all().order_by(*ordering(request, ordering_obj))

        # Здесь фильтры нужны только для вывода формы на страницу
        filters = VehisleFilter(request.GET, queryset=Vehisle.objects.all())

        try:
            paginator = Paginator(vehisles_list, vehisles_per_page)
        except TypeError:
            paginator = Paginator(vehisles_list, 10)
            vehisles_per_page = 10

    page_num = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    penultimate_page = page_obj.paginator.num_pages - 1

    if request.GET.get('filters_status') == 'on':
        try:  # Проверка на существование переменных с результатами фильтрации
            context['filter_res_count'] = filter_res_count
        except UnboundLocalError:  # Если ничего нет, то в шаблон передается ошибка вместо результатов
            context['filter_res_error'] = filter_res_error

    context.update({
        'page_obj': page_obj,
        'penultimate_page': penultimate_page,
        'vehisles_per_page': vehisles_per_page,
        'filters': filters,
        'ordering_obj': ordering_obj,
    })

    return render(request, 'delivery/vehisles.html', context)


def vehisle_single(request, pk):
    vehisle = get_object_or_404(Vehisle, pk=pk)

    context = {
        'vehisle': vehisle,
    }

    return render(request, 'delivery/vehisle-single.html', context)


def create_vehisle(request):

    if request.user.has_perm('delivery.add_vehisle'):

        form = CreateVehisleForm(data=request.POST or None)

        if request.method == 'POST' and form.is_valid() and request.user.has_perm('delivery.add_vehisle'):
            form = CreateVehisleForm(request.POST, request.FILES)
            created_vehisle = form.save()
            created_vehisle.save()
            return redirect('control')

        context = {'form': form}

        return render(request, 'delivery/create-model.html', context)

    else:
        return redirect('index')


def delete_vehisle(request, pk):
    vehisle = Vehisle.objects.get(pk=pk)

    if request.user.has_perm('delivery.delete_vehisle'):
        vehisle.delete()

    return redirect('control')


def change_vehisle(request, pk):
    if request.user.has_perm('delivery.change_vehisle'):
        context = {}

        vehisle = get_object_or_404(Vehisle, pk=pk)

        form = CreateVehisleForm(data=request.POST or None, instance=vehisle)

        if request.method == 'POST' and form.is_valid():
            form = CreateVehisleForm(
                request.POST, request.FILES, instance=vehisle)
            form.save()

            return redirect('control')

        context['form'] = form

        return render(request, 'delivery/create-model.html', context)
    else:
        return redirect('index')


def create_delivery_class(request):

    if request.user.has_perm('delivery.add_deliveryclass'):

        form = CreateDeliveryClassForm(data=request.POST or None)

        if request.method == 'POST' and form.is_valid() and request.user.has_perm('delivery.add_deliveryclass'):
            form = CreateDeliveryClassForm(request.POST)
            created_delivery_class = form.save()
            created_delivery_class.save()
            return redirect('control')

        context = {'form': form}

        return render(request, 'delivery/create-model.html', context)

    else:
        return redirect('index')


def delete_delivery_class(request, pk):
    delivery_class = DeliveryClass.objects.get(pk=pk)

    if request.user.has_perm('delivery.delete_deliveryclass'):
        delivery_class.delete()

    return redirect('control')


def change_delivery_class(request, pk):
    if request.user.has_perm('delivery.change_deliveryclass'):
        context = {}

        delivery_class = get_object_or_404(DeliveryClass, pk=pk)

        form = CreateDeliveryClassForm(
            data=request.POST or None, instance=delivery_class)

        if request.method == 'POST' and form.is_valid():
            form = CreateDeliveryClassForm(
                request.POST, request.FILES, instance=delivery_class)
            form.save()

            return redirect('control')

        context['form'] = form

        return render(request, 'delivery/create-model.html', context)
    else:
        return redirect('index')


def show_quick_quote(request, pk):
    if request.user.has_perm('delivery.view_quickquote'):
        context = {}

        quote_content = get_object_or_404(QuickQuote, pk=pk)
        quote = {}
        fields = quote_content.__dict__

        for field, value in fields.items():
            if field != '_state' and field != 'id' and field != 'user_id':
                quote[str(field)] = value

        context['quote'] = quote
        context['quote_id'] = quote_content.pk

        return render(request, 'delivery/quick-quote.html', context)
    else:
        return redirect('index')


def delete_quick_quote(request, pk):
    if request.user.has_perm('delivery.delete_quickquote'):
        quick_quote = get_object_or_404(QuickQuote, pk=pk)
        quick_quote.delete()

        return redirect('control')
    else:
        return redirect('index')
