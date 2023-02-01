from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            "post_title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название статьи'
            }),
            "post_text": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст статьи'
            }),
            "post_photo": forms.ClearableFileInput(attrs={
                'class': 'ImageField',
            }),
            "post_author": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя Автора'
            })
        }
