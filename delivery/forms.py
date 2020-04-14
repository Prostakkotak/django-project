from django import forms
from .models import QuickQuote, NewsComment

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