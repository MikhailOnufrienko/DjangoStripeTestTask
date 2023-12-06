from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Item


@register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    empty_value_display = '-empty-'
    search_fields = ('name', )
