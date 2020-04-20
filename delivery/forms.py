from django import forms
from tinymce.widgets import  TinyMCE
from .models import QuickQuote, NewsComment, ProposedNews

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