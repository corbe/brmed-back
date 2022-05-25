# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

class Currency(models.Model):
    id = models.UUIDField(primary_key=True,  default=uuid.uuid4, null=False, blank=True, editable=False)
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Rate(models.Model):
    id = models.UUIDField(primary_key=True,  default=uuid.uuid4, null=False, blank=True, editable=False)    
    date = models.DateField('Date')
    base_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='base_currency')

    def __str__(self):
        return self.date
    

class RateValue(models.Model):
    id = models.UUIDField(primary_key=True,  default=uuid.uuid4, null=False, blank=True, editable=False)  
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency')
    value = models.DecimalField(max_digits=6, decimal_places=2)
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE, related_name='rate')
    
    def __str__(self):
        return self.currency.name
