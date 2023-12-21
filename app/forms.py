"""
Definition of forms.
"""

from random import choice
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog
from .models import Order



class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))


class AnketaForm(forms.Form):
    name = forms.CharField(label="Ваше имя", min_length=2, max_length=100)
    city = forms.CharField(label="Ваш город", min_length=2, max_length=100)
    grade = forms.ChoiceField(label="Оценка",
                             choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                             widget=forms.RadioSelect, initial=1)

    email = forms.EmailField(label='Ваш e-mail', min_length=7)
    message = forms.CharField(label='Отзыв',
                              widget=forms.Textarea(attrs={'rows': 12, 'cols':20}))
    
class CommentForm (forms.ModelForm):

    class Meta:
        model = Comment # используемая модель

        fields = ('text',) # требуется заполнить только поле text

        labels = {'text': "Комментарий"} # метка к полю формы text


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 
                  'content': "Полное содержание", 'image': "Картинка"}

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'address']