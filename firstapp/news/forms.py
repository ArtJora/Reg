# -*- coding: utf-8 -*-

from django.forms import ModelForm
from models import Comments, Article
from django import forms

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']

# class NewsForm(ModelForm):
#     class Meta:
#         model = Article
#         fields = '__all__'

class NewsForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["article_title", "article_text"]
    article_title = forms.CharField(
        label='Заголовок новости',
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    article_text = forms.CharField(
        label='Текст новости',
        widget=forms.Textarea(attrs={'class':'form-control input-lg',})
    )
    # article_date = forms.DateField(
    #     label='Дата публикации',
    #     widget=forms.DateTimeInput(attrs={'class':'form-control','input type':'date'})
    # )