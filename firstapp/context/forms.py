# -*- coding: utf-8 -*-
from django import forms
from models import Context_dancer, Context

from django.contrib import auth

class ContextDancerForm(forms.ModelForm):
    class Meta:
        model = Context_dancer
        fields = ['context_dancer_name','context_dance_program','context_age_category','context_dance_league']
        # fields = '__all__'

    context_dancer_name = forms.CharField(
        label='Имя танцора',
        required=True,
        widget=forms.TextInput(attrs={'type':'text',
                                      'cols': '45',
                                      'required':'True',
                                      'name':'search',
                                      'class':'form-control ',
                                      'id':'context_dancer_name',
                                      'placeholder':'Введите имя танцора',
                                      'list':'search-results',
                                      'value':'',
                                      'autocomplete':'off'})
    )
    context_dancer_name2 = forms.CharField(
        label='Имя танцора',
        required=False,
        widget=forms.TextInput(attrs={'type':'text',
                                      'name':'search',
                                      'class':'form-control',
                                      'id':'context_dancer_name2_duet',
                                      'placeholder':'Введите имя танцора',
                                      'list':'search-results2_duet',
                                      'value':'',
                                      'autocomplete':'off'})
    )


    context_dancer_name3 = forms.CharField(
        label='Имя танцора',
        required=False,
        widget=forms.TextInput(attrs={'type':'text',
                                      'name':'search',
                                      'class':'form-control',
                                      'id':'context_dancer_name3_duet',
                                      'placeholder':'Введите имя танцора',
                                      'list':'search-results3_duet',
                                      'value':'',
                                      'autocomplete':'off'})
    )


    context_dancer_name4 = forms.CharField(
        label='Имя танцора',
        required=False,
        widget=forms.TextInput(attrs={'type':'text',
                                      'name':'search',
                                      'class':'form-control',
                                      'id':'context_dancer_name4_duet',
                                      'placeholder':'Введите имя танцора',
                                      'list':'search-results4_duet',
                                      'value':'',
                                      'autocomplete':'off'})
    )


    context_dancer_name5 = forms.CharField(
        label='Имя танцора',
        required=False,
        widget=forms.TextInput(attrs={'type':'text',
                                      'name':'search',
                                      'class':'form-control',
                                      'id':'context_dancer_name5_duet',
                                      'placeholder':'Введите имя танцора',
                                      'list':'search-results5_duet',
                                      'value':'',
                                      'autocomplete':'off'})
    )


    context_dancer_name6 = forms.CharField(
        label='Имя танцора',
        required=False,
        widget=forms.TextInput(attrs={'type':'text',
                                      'name':'search',
                                      'class':'form-control',
                                      'id':'context_dancer_name6_duet',
                                      'placeholder':'Введите имя танцора',
                                      'list':'search-results6_duet',
                                      'value':'',
                                      'autocomplete':'off'})
    )


    context_dancer_name7 = forms.CharField(
        label='Имя танцора',
        required=False,
        widget=forms.TextInput(attrs={'type':'text',
                                      'name':'search',
                                      'class':'form-control',
                                      'id':'context_dancer_name7_duet',
                                      'placeholder':'Введите имя танцора',
                                      'list':'search-results7_duet',
                                      'value':'',
                                      'autocomplete':'off'})
    )



    context_dance_program = forms.CharField(
        label='Танцевальная программа',
        widget=forms.TextInput(attrs={'type':'text',
                                      'name':'context_dance_program',
                                      'class':'form-control',
                                      'required':'True',
                                      'id':'context_dance_program',
                                      'placeholder':'Выберите танцевальную программу',
                                      'list':'search-results1',
                                      'value':'',
                                      'autocomplete':'off'})
    )
    context_age_category = forms.CharField(
        label='Возрастная категория',
        widget=forms.TextInput(attrs={'type':'text',
                                      'required':'True',
                                      'name':'context_age_category',
                                      'class':'form-control',
                                      'id':'context_age_category',
                                      'placeholder':'Выберите танцевальную программу',
                                      'list':'search-results2',
                                      'value':'',
                                      'autocomplete':'off'})
    )
    context_dance_league = forms.CharField(
        label='Возрастная категория',
        required=False,
        widget=forms.TextInput(attrs={'type':'text',
                                      'required':'True',
                                      'name':'context_dance_league',
                                      'class':'form-control',
                                      'id':'context_dance_league',
                                      'placeholder':'Выберите танцевальную программу',
                                      'list':'search-results3',
                                      'value':'',
                                      'autocomplete':'off'})
    )
class ContextContentForm(forms.ModelForm):
    class Meta:
        model = Context
        # fields = ['context_name','context_dance_programm','context_age_category','context_dance_league']
        fields = '__all__'
    context_date = forms.DateField(
        label='Дата',
        widget=forms.DateTimeInput(attrs={'class':'form-control','input type':'date'})
    )



class ContextDuetForm(forms.ModelForm):
    class Meta:
        model = Context_dancer
        fields = ['context_dancer_name','context_dance_program','context_age_category']
        # fields = '__all__'

    context_dancer_name = forms.CharField(
        label='Имя танцора',
        required=True,
        widget=forms.TextInput(attrs={'type':'text',
                                      'required':'True',
                                      'name':'search',
                                      'class':'form-control',
                                      'id':'context_dancer_name_duet',
                                      'placeholder':'Введите имя танцора',
                                      'list':'search-results_duet',
                                      'value':'',
                                      'autocomplete':'off'})
    )

    context_dancer_name2 = forms.CharField(
        label='Имя танцора',
        required=False,
        widget=forms.TextInput(attrs={'type':'text',
                                      'name':'search',
                                      'class':'form-control',
                                      'id':'context_dancer_name2_duet',
                                      'placeholder':'Введите имя танцора',
                                      'list':'search-results2_duet',
                                      'value':'',
                                      'autocomplete':'off'})
    )

    context_dance_program = forms.CharField(
        label='Танцевальная программа',
        widget=forms.TextInput(attrs={'type':'text',
                                      'name':'context_dance_program_duet',
                                      'class':'form-control',
                                      'required':'True',
                                      'id':'context_dance_program_duet',
                                      'placeholder':'Выберите танцевальную программу',
                                      'list':'context_dance_program_duet-results',
                                      'value':'',
                                      'autocomplete':'off'})
    )
    context_age_category = forms.CharField(
        label='Возрастная категория',
        widget=forms.TextInput(attrs={'type':'text',
                                      'required':'True',
                                      'name':'context_age_category_duet',
                                      'class':'form-control',
                                      'id':'context_age_category_duet',
                                      'placeholder':'Выберите танцевальную программу',
                                      'list':'context_age_category_duet-results',
                                      'value':'',
                                      'autocomplete':'off'})
    )
    # context_dance_league = forms.CharField(
    #     label='Возрастная категория',
    #     widget=forms.TextInput(attrs={'type':'text',
    #                                   'required':'True',
    #                                   'name':'context_dance_league_duet',
    #                                   'class':'form-control',
    #                                   'id':'context_dance_league_duet',
    #                                   'placeholder':'Выберите танцевальную программу',
    #                                   'list':'context_dance_league_duet-results',
    #                                   'value':'',
    #                                   'autocomplete':'off'})
    # )
