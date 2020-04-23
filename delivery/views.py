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
        quick_quote_form.save()
        '''
        Редирект здесь нужен для сброса типа запроса,
        без этого при каждом обновлении страницы тип запроса будет POST,
        что приведет к отправке формы при каждом обновлении
        '''
        return redirect('index')

    return render(request, 'delivery/index.html', context={
        'vehisle_list': vehisle_list,
        'delivery_class_list': delivery_class_list,
        'news_list': news_list,
        'quick_quote_form': quick_quote_form,
    })


def control(request):
    context = {
        'proposed_news_count': ProposedNews.objects.all().count(),
        'quick_quote_count': QuickQuote.objects.all().count(),
        'news_count': News.objects.all().count(),
        'vehisles_count': Vehisle.objects.all().count(),
        'delivery_class_count': DeliveryClass.objects.all().count(),
    }

    return render(request, 'delivery/control-panel.html', context)


def create_news(request):
    form = CreateNewsForm(data=request.POST or None)

    if request.method == 'POST' and form.is_valid() and request.user.has_perm('delivery.add_news'):
        created_news = form.save()
        created_news.user = request.user
        created_news.title_image = request.POST.get('title_image')
        created_news.save()
        return redirect('control')


    context = {'form':form}

    return render(request, 'delivery/create-news.html', context)


def create_vehisle(request):
    form = CreateVehisleForm(data=request.POST or None)

    if request.method == 'POST' and form.is_valid() and request.user.has_perm('delivery.add_vehisle'):
        form.save()
        return redirect('control')


    context = {'form':form}

    return render(request, 'delivery/create-vehisle.html', context)


def create_delivery_class(request):
    form = CreateDeliveryClassForm(data=request.POST or None)

    if request.method == 'POST' and form.is_valid() and request.user.has_perm('delivery.add_deliveryclass'):
        form.save()
        return redirect('control')


    context = {'form':form}

    return render(request, 'delivery/create-delivery-class.html', context)


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
        proposed_news = form.save()
        proposed_news.user = request.user
        proposed_news.title_image = request.POST.get('title_image')
        proposed_news.save()

        return redirect('news')

    context.update({
        'form': form,
    })

    return render(request, 'delivery/create-news.html', context)


def news_single_delete(request, pk):
    news = News.objects.get(pk=pk)

    if request.user.has_perm('delivery.delete_news') or request.user.pk == news.user.pk:
        news.delete()

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
            timezone.now() - timezone.timedelta(days=7), timezone.now() + \
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

    if request.GET.get('filters_status') == 'on':
        filters = VehisleFilter(
            request.GET, queryset=Vehisle.objects.all().order_by(
                *ordering(request, ordering_obj))
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
