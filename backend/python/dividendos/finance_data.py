from django.http import JsonResponse
from django.views import View
from .models import DividendoModel
from datetime import datetime
import requests
import json  # Import the json module
import yfinance as yf


class LoadYahooFinanceData(View):
    def get(self, request):

        ticker = "PETR4.SA"

        stock = yf.Ticker(ticker)

        dividends = stock.dividends

        print(dividends)

        data_to_return = {
            'message': 'Dados carregados com sucesso.',
            'symbol': ticker,
            'dividend_date': dividends.index[-1].strftime('%Y-%m-%d'),
            'dividend_amount': dividends[-1],
        }

        json_data = json.dumps(data_to_return)

        return JsonResponse(json_data, safe=False)
