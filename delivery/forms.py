from django import forms
from tinymce.widgets import  TinyMCE
from .models import QuickQuote, NewsComment, ProposedNews, News, Vehisle, DeliveryClass

class QuickQuoteForm(forms.ModelForm):
    class Meta:
        model = QuickQuote
        fields = (
            'name',
            'subject',
            'email',
            'phone',
            'service',
            'message',
        )

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'customer-action__input',
                'value': '',
                'placeholder': 'Your name'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'customer-action__input',
                'value': '',
                'placeholder': 'Subject'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'customer-action__input',
                'value': '',
                'placeholder': 'E-Mail adress'
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'customer-action__input',
                'value': '',
                'placeholder': 'Phone number'
            }),
            'service': forms.TextInput(attrs={
                'class': 'customer-action__input customer-action__input_extended',
                'value': '',
                'placeholder': 'Service'
            }),
            'message': forms.Textarea(attrs={
                'class': 'customer-action__message',
                'value': '',
                'placeholder': 'Your message'
            }),
        }


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = (
            'title',
            'title_image',
            'short_description',
            'content',
            'important_status',
            'tags',
        )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'create-news-form__input',
                'placeholder': 'News title',
            }),
            'title_image': forms.FileInput(attrs={
                'class': 'create-news-form__image-input',
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'create-news-form__input',
                'placeholder': 'News short description',
            }),
            'content': TinyMCE(attrs={
                'class': 'create-news-form__textarea',
                'placeholder': 'Your content',
            }),
        }


class CreateVehisleForm(forms.ModelForm):
    class Meta:
        model = Vehisle
        fields = (
            'model',
            'kind_of_vehisle',
            'photo',
            'can_be_booked',
            'delivery_method',
            'status',
            'price_per_use',
            'price_per_km',
            'km_per_day',
            'maximum_load',
            'cargo_volume',
        )


class CreateDeliveryClassForm(forms.ModelForm):
    class Meta:
        model = DeliveryClass
        fields = (
            'delivery_class',
            'price_multiplier',
        )


class NewsProposeForm(forms.ModelForm):
    class Meta:
        model = ProposedNews
        fields = (
            'title',
            'title_image',
            'short_description',
            'content',
            'important_status',
            'tags',
        )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'offer-news-form__input',
                'placeholder': 'News title',
            }),
            'title_image': forms.FileInput(attrs={
                'class': 'offer-news-form__image-input',
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'offer-news-form__input',
                'placeholder': 'News short description',
            }),
            'content': TinyMCE(attrs={
                'class': 'offer-news-form__textarea',
                'placeholder': 'Your content',
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'offer-news-form__checkbox'
            }),
        }


class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = NewsComment
        fields = (
            'message',
        )
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'news-comments__textarea',
                'placeholder': 'Your message'
            })
        }