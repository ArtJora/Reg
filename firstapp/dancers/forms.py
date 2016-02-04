# -*- coding: utf-8 -*-
from django import forms
from models import Dancer
from django.contrib import auth

class DancerForm(forms.ModelForm):
    class Meta:
        model = Dancer
        fields = ["dancer_name", "dancer_birthday", "dancer_balls"]
    dancer_name = forms.CharField(
        label='Имя танцора',
        widget=forms.TextInput(attrs={'class':'form-control',
                                      'required':'True',
                                      'value':'',
                                      'autocomplete':'off'})
    )
    dancer_birthday = forms.DateField(
        label='день рождения',
        widget=forms.DateTimeInput(attrs={'class':'form-control',
                                          'required':'True',
                                          'input type':'date'}),
        required=False
    )
    dancer_balls = forms.IntegerField(
        label='колво балов',
        widget=forms.NumberInput(attrs={'value':'0',
                                        'required':'True',
                                        'class':'form-control'})
    )