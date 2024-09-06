from django.shortcuts import render
from .models import Currency, ExchangeRate
from decimal import Decimal, ROUND_HALF_UP

def convert_currency(request):
    currencies = Currency.objects.all()  # Fetch all currencies

    if request.method == 'POST':
        amount = Decimal(request.POST['amount'])
        base_currency_code = request.POST['base_currency']
        target_currency_code = request.POST['target_currency']

        base_currency = Currency.objects.get(currency_code=base_currency_code)
        target_currency = Currency.objects.get(currency_code=target_currency_code)
        
        try:
            exchange_rate = ExchangeRate.objects.get(
                base_currency_id=base_currency.id,
                target_currency_id=target_currency.id
            )
        except ExchangeRate.DoesNotExist:
            return render(request, 'coin_converter/convert.html', {
                'currencies': currencies,
                'error': 'Exchange rate not found.'
            })

        rate = Decimal(exchange_rate.rate)
        converted_amount = (amount * rate).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

        return render(request, 'coin_converter/convert.html', {
            'currencies': currencies,
            'converted_amount': converted_amount,
            'base_currency': base_currency_code,
            'target_currency': target_currency_code
        })

    return render(request, 'coin_converter/convert.html', {
        'currencies': currencies
    })
