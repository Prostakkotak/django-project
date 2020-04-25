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
                'class': 'create-model-form__input',
                'placeholder': 'News title',
            }),
            'title_image': forms.FileInput(attrs={
                'class': 'create-model-form__image-input',
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'create-model-form__input',
                'placeholder': 'News short description',
            }),
            'content': TinyMCE(attrs={
                'class': 'create-model-form__textarea',
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

        widgets = {
            'model': forms.TextInput(attrs={
                'class': 'create-model-form__input'
            }),
            'kind_of_vehisle': forms.TextInput(attrs={
                'class': 'create-model-form__input'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'create-model-form__input'
            }),
            'can_be_booked': forms.CheckboxInput(attrs={
                'class': 'create-model-form__input'
            }),
            'delivery_method': forms.Select(attrs={
                'class': 'create-model-form__input'
            }),
            'status': forms.Select(attrs={
                'class': 'create-model-form__input'
            }),
            'price_per_use': forms.NumberInput(attrs={
                'class': 'create-model-form__input'
            }),
            'price_per_km': forms.NumberInput(attrs={
                'class': 'create-model-form__input'
            }),
            'km_per_day': forms.NumberInput(attrs={
                'class': 'create-model-form__input'
            }),
            'maximum_load': forms.NumberInput(attrs={
                'class': 'create-model-form__input'
            }),
            'cargo_volume': forms.NumberInput(attrs={
                'class': 'create-model-form__input'
            }),
        }


class CreateDeliveryClassForm(forms.ModelForm):
    class Meta:
        model = DeliveryClass
        fields = (
            'delivery_class',
            'price_multiplier',
        )

        widgets = {
            'delivery_class': forms.TextInput(attrs={
                'class': 'create-model-form__input'
            }),
            'price_multiplier': forms.NumberInput(attrs={
                'class': 'create-model-form__input'
            })
        }


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
                'class': 'create-model-form__input',
                'placeholder': 'News title',
            }),
            'title_image': forms.FileInput(attrs={
                'class': 'create-model-form__image-input',
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'create-model-form__input',
                'placeholder': 'News short description',
            }),
            'content': TinyMCE(attrs={
                'class': 'create-model-form__textarea',
                'placeholder': 'Your content',
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'create-model-form__checkbox'
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