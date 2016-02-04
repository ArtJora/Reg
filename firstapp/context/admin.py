# -*- coding: utf-8 -*-
from django.contrib import admin
from context.models import Context, Dance_program, Age_category, Dance_league, Context_dancer
# Register your models here.

class ContextAdmin(admin.ModelAdmin):

    fields = ['context_name',
              'context_date',
              'context_place',
              'context_organizer',
              'context_sity',
              'context_dance_program',
              'context_age_category',
              'context_dance_league' ]
    list_display = [
        'context_name',
        'context_date',
        'context_place',
        'context_organizer',
        'context_sity',
    ]
    raw_id_fields = [ 'context_dance_program',
                      'context_age_category',
                      'context_dance_league']
admin.site.register(Context, ContextAdmin)

class Dance_program_Admin(admin.ModelAdmin):
    fields = ['dance_program_name']
    list_display = [
        'dance_program_name',
    ]
    search_fields = ('dance_program_name',)
    ordering = ('dance_program_name',)


admin.site.register(Dance_program, Dance_program_Admin)

class Age_category_Admin(admin.ModelAdmin):
    fields = ['age_category_name']
    list_display = [
        'age_category_name',
    ]
admin.site.register(Age_category, Age_category_Admin)

class Dance_league_Admin(admin.ModelAdmin):
    fields = ['dance_league_name']
    list_display = [
        'dance_league_name',
    ]
admin.site.register(Dance_league, Dance_league_Admin)

class Context_dancer_Admin(admin.ModelAdmin):
    fields = ['context_dancer_name','context_dancer_treaner','context_dance_program','context_age_category','context_dance_league','context_name']
    # raw_id_fields = ('context_dancer_treaner','context_dance_program','context_age_category','context_dance_league','context_name',)
    list_display = [
        'context_dancer_name',
        'context_dancer_treaner',
        'context_dance_program',
        'context_age_category',
        'context_dance_league',
        'context_name'
    ]

admin.site.register(Context_dancer, Context_dancer_Admin)