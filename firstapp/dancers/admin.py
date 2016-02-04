from django.contrib import admin
from dancers.models import Dancer

# Register your models here.
class DancerAdmin(admin.ModelAdmin):
    fields = ['dancer_name', 'dancer_birthday', 'dancer_trainer', 'dancer_balls']
    list_filter = ['dancer_name']
    list_display = [
        'dancer_name',
        'dancer_birthday',
        'dancer_trainer',
        'dancer_balls',
    ]

admin.site.register(Dancer, DancerAdmin)
