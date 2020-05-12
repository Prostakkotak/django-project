from django.shortcuts import render, get_object_or_404, Http404, redirect
from .models import Vehisle, DeliveryClass, News, QuickQuote, NewsTag, NewsComment, ProposedNews
from .models import DeliveryOrder as DeliveryOrderModel
from .forms import QuickQuoteForm, NewsCommentForm, NewsProposeForm, CreateNewsForm, CreateDeliveryClassForm, CreateVehisleForm
from .filters import VehisleFilter
from .ordering import ordering
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F, Q
from django.utils import timezone
from django.views.generic import View
from django.contrib import messages


class Index(View):
    def get(self, request):
        vehisle_list = Vehisle.objects.all()[:5]
        delivery_class_list = DeliveryClass.objects.all()
        news_list = News.objects.all()[:3]

        quick_quote_form = QuickQuoteForm()

        return render(request, 'delivery/index.html', context={
            'vehisle_list': vehisle_list,
            'delivery_class_list': delivery_class_list,
            'news_list': news_list,
            'quick_quote_form': quick_quote_form,
        })

    def post(self, request):
        quick_quote_form = QuickQuoteForm(data=request.POST)

        if quick_quote_form.is_valid():
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

                messages.success(request, 'Your question successfully sended')
                return redirect('index')
            else:
                messages.warning(
                    request, 'Your accound don\'t have an access to do it')
                return redirect('index')
        else:
            messages.warning(
                request, 'Please check that the filling is correct')
            return redirect('index')


class DeliveryOrder(View):
    def get(self, request):
        if request.user.has_perm('delivery.add_deliveryorder'):
            context = {}

            maximum_load_max = 0
            cargo_volume_max = 0

            for item in Vehisle.objects.all():
                if item.maximum_load > maximum_load_max:
                    maximum_load_max = item.maximum_load
                if item.cargo_volume > cargo_volume_max:
                    cargo_volume_max = item.cargo_volume

            if request.GET.get('confirmation') == 'on':
                choosed_vehisle = Vehisle.objects.get(
                    pk=request.GET.get('vehisle'))
                choosed_delivery_class = DeliveryClass.objects.get(
                    pk=request.GET.get('delivery_class'))

                delivery_request = DeliveryOrderModel()
                delivery_request.user = request.user
                delivery_request.cost = choosed_delivery_class.price_multiplier * ((int(request.GET.get('path_length')) *
                                                                                    choosed_vehisle.price_per_km) + choosed_vehisle.price_per_use)

                delivery_request.package_volume = request.GET.get(
                    'package_volume')
                delivery_request.package_weight = request.GET.get(
                    'package_weight')
                delivery_request.path_length = request.GET.get('path_length')

                delivery_request.vehisle = choosed_vehisle
                delivery_request.delivery_class = choosed_delivery_class

                delivery_request.save()

                return redirect('index')

            elif request.GET.get('check_conditions') == 'on':
                choosed_vehisle = Vehisle.objects.get(
                    pk=request.GET.get('vehisle'))
                choosed_delivery_class = DeliveryClass.objects.get(
                    pk=request.GET.get('delivery_class'))

                delivery_cost = choosed_delivery_class.price_multiplier * ((int(request.GET.get('path_length')) *
                                                                            choosed_vehisle.price_per_km) + choosed_vehisle.price_per_use)

                context.update({
                    'choosed_vehisle': choosed_vehisle.model,
                    'choosed_delivery_class': choosed_delivery_class.delivery_class,
                    'delivery_cost': delivery_cost,
                })

            elif request.GET.get('delivery_info') == 'exists':
                vehisles_list = Vehisle.objects.filter(
                    delivery_method=request.GET.get('delivery_method'),
                    maximum_load__range=[
                        request.GET.get('package_weight'), maximum_load_max
                    ],
                    cargo_volume__range=[
                        request.GET.get('package_volume'), cargo_volume_max
                    ],
                    status='a'
                )

                if len(vehisles_list) != 0:
                    context['vehisles_list'] = vehisles_list

                    context['price_multiplier'] = DeliveryClass.objects.get(
                        pk=request.GET.get('delivery_class')).price_multiplier

                else:
                    context['error_msg'] = 'Sorry, no vehisles were found by your request'

            context.update({
                'delivery_class_list': DeliveryClass.objects.all(),
            })

            return render(request, 'delivery/delivery-order.html', context)
        else:
            return redirect('index')


# Миксина для удаления экземпляров моделей
class DeleteModelMixin:
    model = None

    def get(self, request, pk):
        if request.user.has_perm('delivery.delete_' + self.model.__name__.lower()):
            deleting_model = get_object_or_404(self.model, pk=pk)
            deleting_model.delete()

            if request.GET.get('next'):
                return redirect(request.GET.get('next'))

            return redirect('control')


class DeleteDeliveryOrder(DeleteModelMixin, View):
    model = DeliveryOrderModel


class DeleteSingleNews(DeleteModelMixin, View):
    model = News


class DeleteProposedNews(DeleteModelMixin, View):
    model = ProposedNews


class DeleteDeliveryClass(DeleteModelMixin, View):
    model = DeliveryClass


class DeleteVehisle(DeleteModelMixin, View):
    model = Vehisle


class DeleteQuickQuote(DeleteModelMixin, View):
    model = QuickQuote


class DeleteNewsComment(View):
    def get(self, request, pk):
        comment = NewsComment.objects.get(pk=pk)

        if request.user.has_perm('delivery.delete_newscomment') or comment.user.pk == request.user.pk:
            comment.delete()

        return_path = request.META.get('HTTP_REFERER', '/')
        return redirect(return_path)


class ShowDeliveryOrder(View):
    def get(self, request, pk):
        if request.user.has_perm('delivery.view_deliveryorder'):
            context = {}

            delivery_order = get_object_or_404(DeliveryOrderModel, pk=pk)
            model_info = {}
            fields = delivery_order.__dict__

            for field, value in fields.items():
                if field != '_state' and field != 'id' and field != 'user_id':
                    model_info[str(field)] = value

            context['model_info'] = model_info
            context['model_id'] = delivery_order.pk
            context['model_type'] = 'delivery_order'

            return render(request, 'delivery/model-info.html', context)
        else:
            return redirect('index')


class Control(View):
    def get(self, request):
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
            'delivery_order_list': DeliveryOrderModel.objects.all(),
            'delivery_order_count': DeliveryOrderModel.objects.all().count(),
        }

        return render(request, 'delivery/control-panel.html', context)


class Registration(View):
    def get(self, request):
        form = UserCreationForm()

        return render(request, 'registration/registration.html', context={
            'form': form,
        })

    def post(self, request):
        form = UserCreationForm(data=request.POST or None)

        if form.is_valid():
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

            # Логиним пользователя после успешной регистрации
            login(request, user)

            return redirect('index')

        return render(request, 'registration/registration.html', context={
            'form': form,
        })


class NewsSingle(View):
    def get(self, request, pk):
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

    def post(self, request, pk):
        news_content = get_object_or_404(News, pk=pk)
        news_comment_form = NewsCommentForm(data=request.POST)

        if news_comment_form.is_valid():
            news_comment = news_comment_form.save(commit=False)
            news_comment.user = request.user

            if request.POST.get('answer'):
                news_comment.answer = get_object_or_404(
                NewsComment, pk=int(request.POST.get('answer')))

            news_comment.news = news_content

            news_comment.save()
            return redirect('news_single', pk=pk)
        else:
            messages.warning(request, 'something went wrong, sorry')
            return redirect('news_single', pk=pk)



class AddModelMixin:
    create_form = None
    model = None

    def get(self, request):

        if request.user.has_perm('delivery.add_' + self.model.__name__.lower()):
            context = {}

            form = self.create_form()

            context.update({
                'form': form,
            })

            return render(request, 'delivery/create-model.html', context)
        else:
            return redirect('index')

    def post(self, request):
        form = self.create_form(request.POST, request.FILES)

        if form.is_valid() and request.user.has_perm('delivery.add_' + self.model.__name__.lower()):
            created_model = form.save()
            
            try:
                created_model.user = request.user
            except AttributeError:
                pass

            created_model.save()

            return redirect('control')


class OfferNews(AddModelMixin, View):
    create_form = NewsProposeForm
    model = ProposedNews

class CreateDeliveryClass(AddModelMixin, View):
    create_form = CreateDeliveryClassForm
    model = DeliveryClass

class CreateNews(AddModelMixin, View):
    create_form = CreateNewsForm
    model = News

class CreateVehisle(AddModelMixin, View):
    create_form = CreateVehisleForm
    model = Vehisle


def proposed_news_demo(request, pk):
    news_content = get_object_or_404(ProposedNews, pk=pk)

    context = {
        'news_content': news_content,
    }

    return render(request, 'delivery/propose-news-demo.html', context)


class ConfirmedProposedNews(View):
    def get(self, request, pk):
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


class NewsPage(View):
    def get(self, request):

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


class VehislesPage(View):
    def get(self, request):
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


class VehisleSingle(View):
    def get(self, request, pk):
        vehisle = get_object_or_404(Vehisle, pk=pk)

        context = {
            'vehisle': vehisle,
        }

        return render(request, 'delivery/vehisle-single.html', context)


class ChangeModelMixin:
    model = None
    model_form = None

    def get(self, request, pk):
        if request.user.has_perm('delivery.change_' + self.model.__name__.lower()):
            context = {}

            model_change = get_object_or_404(self.model, pk=pk)

            form = self.model_form(instance=model_change)

            context['form'] = form

            return render(request, 'delivery/create-model.html', context)
        else:
            return redirect('index')

    def post(self, request, pk):
        model_change = get_object_or_404(self.model, pk=pk)

        form = self.model_form(data=request.POST or None, instance=model_change)

        if request.method == 'POST' and form.is_valid():
            form = self.model_form(
                request.POST, request.FILES, instance=model_change)
            form.save()

            return redirect('control')

class ChangeNews(ChangeModelMixin, View):
    model = News
    model_form = CreateNewsForm

class ChangeVehisle(ChangeModelMixin, View):
    model = Vehisle
    model_form = CreateVehisleForm

class ChangeDeliveryClass(ChangeModelMixin, View):
    model = DeliveryClass
    model_form = CreateDeliveryClassForm


class ShowQuickQuote(View):
    def get(self, request, pk):
        if request.user.has_perm('delivery.view_quickquote'):
            context = {}

            quote_content = get_object_or_404(QuickQuote, pk=pk)
            quote = {}
            fields = quote_content.__dict__

            for field, value in fields.items():
                if field != '_state' and field != 'id' and field != 'user_id':
                    quote[str(field)] = value

            context['model_info'] = quote
            context['model_id'] = quote_content.pk
            context['model_type'] = 'quick_quote'

            return render(request, 'delivery/model-info.html', context)
        else:
            return redirect('index')
