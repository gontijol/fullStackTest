from django.http import JsonResponse
from django.views import View
from datetime import datetime
import requests
import json  # Import the json module
import yfinance as yf
from .models import DividendoModel


class LoadYahooFinanceData(View):
    def get(self, request):
        ticker = "PETR4.SA"
        year = datetime.now().year
        DividendoModel.buscar_dividendos(symbol=ticker, year=year)
        latest_dividend = DividendoModel.objects.latest('date')

        dividend_amount = float(latest_dividend.amount)

        data_to_return = {
            'message': 'Dados carregados com sucesso.',
            'symbol': ticker,
            'dividend_date': latest_dividend.date.strftime('%Y-%m-%d'),
            'dividend_amount': dividend_amount,
        }

        json_data = json.dumps(data_to_return)

        return JsonResponse(json_data, safe=False)
