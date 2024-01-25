from django.shortcuts import render
import urllib.request
import json

def index(request):
    if request.method == 'POST':
        currency = request.POST['currency']
        exchange = request.POST['exchange']
        quantity = request.POST['quantity']
        url = 'https://v6.exchangerate-api.com/v6/b4e84dfd643af052fa576d52/latest/' + currency
        source = urllib.request.urlopen(url).read()
        data_currency = json.loads(source)
        if float(quantity) >= 0:
            data = {
                'currency': str(currency),
                'CURRENCY': float(data_currency['conversion_rates'][currency]) * float(quantity),
                'EXCHANGE': float(data_currency['conversion_rates'][exchange]) * float(quantity),
                'exchange': str(exchange),
                }
        else:
            return 'Xato'
    else:
        data = {}
    selected = 'selected'
    return render(request, 'index.html', {'data': data, 'selected': selected})
