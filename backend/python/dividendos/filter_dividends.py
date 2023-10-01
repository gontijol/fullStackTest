from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import DividendoModel
from django.db.models import Sum


@method_decorator(csrf_exempt, name='dispatch')
class DividendSummaryByYearPOST(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            symbol = data.get('symbol')
            year = data.get('year')

            if symbol is None or year is None:
                return JsonResponse({'error': 'Parâmetros de símbolo e ano são obrigatórios.'}, status=400)

            dividend_sum = DividendoModel.objects.filter(
                symbol=symbol, date__year=year).aggregate(total_dividend=Sum('amount'))

            total_dividend = dividend_sum['total_dividend'] or 0
            print("Total de dividendos para o ano e símbolo fornecidos:",
                  total_dividend)
            return JsonResponse({'symbol': symbol, 'year': year, 'total_dividend': total_dividend})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
