from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from .models import DividendoModel
from datetime import datetime


class GetDividendsByYear(View):
    def get(self, request):
        symbol = request.GET.get('symbol')
        year = request.GET.get('year')

        if not symbol or not year:
            return HttpResponseBadRequest("Parâmetros obrigatórios não fornecidos.")

        try:
            year = int(year)
        except ValueError:
            return HttpResponseBadRequest("Ano fornecido é inválido.")

        # Consulte o banco de dados para obter os dividendos do símbolo e ano fornecidos
        dividends = DividendoModel.objects.filter(
            symbol=symbol, date__year=year)

        # Calcule o valor total dos dividendos
        total_dividends = sum(dividend.amount for dividend in dividends)

        return JsonResponse({'total_dividends': total_dividends})
