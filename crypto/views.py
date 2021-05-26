from django.shortcuts import render
from .btc_turk_api import Client
from .models import Currency, Price


def main(request):
    client = Client()
    coins = client.get_all_prices()

    for key, values in coins.items():
        try:
            cur = Currency()
            cur.ticker = key
            cur.label = key.split('_')[0]
            cur.save()
        except:
            cur = Currency.objects.filter(ticker=key)[0]

        price = Price()
        price.currency = cur
        price.oopen = values['open']
        price.low = values['low']
        price.high = values['high']
        price.close = values['close']
        price.average = values['average']
        price.volume = values['volume']
        price.save()

    cont = {'msg': 'Hello World!', 'coins': coins}
    return render(request, template_name='main_page.html', context=cont)
