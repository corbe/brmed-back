from django.core.management.base import BaseCommand
from django.conf import settings
import requests
from rates.models import Currency, Rate, RateValue
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Load Rates'
    
    def add_arguments(self, parser):
        parser.add_argument('--base')
        parser.add_argument('--last_days_count')

        
    def handle(self, base, last_days_count, *args, **kwargs):

        if not last_days_count:
            last_days_count = 10
        
        if not base:
            base = 'USD'

        today = datetime.now()
            
        for date in (today - timedelta(n) for n in range(int(last_days_count))):
            date = datetime.strftime(date,'%Y-%m-%d')
            
            url = settings.VATCOMPLY_URL + '/rates?base=%s&date=%s' % (base, date)
            r = requests.get(url)
            data = r.json()
        
            for currency in Currency.objects.all():

                value = data['rates'][currency.name]

                base_currency=Currency.objects.get(name=base)
                currency=Currency.objects.get(name=currency.name)
                
                rate, created = Rate.objects.get_or_create(
                    date=date,
                    base_currency=base_currency,
                    defaults={
                        'date': date,
                        'base_currency': base_currency
                    }
                )
          
                RateValue.objects.get_or_create(
                    currency=currency,
                    rate=rate,
                    defaults={
                        'rate': rate,
                        'currency': currency,
                        'value': value
                    }
                )
