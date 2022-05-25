# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Currency, Rate, RateValue

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')


class RateAdmin(admin.ModelAdmin):
    list_display = ('date', 'base_currency')

class RateValueAdmin(admin.ModelAdmin):
    list_display = ('rate', 'currency', 'value')


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(RateValue, RateValueAdmin)
