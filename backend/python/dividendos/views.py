from .models import DividendoModel  # Adicione esta linha

from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from .models import DividendoModel
from django.views.decorators.csrf import csrf_exempt


class DividendoAPI(View):
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        # Lógica para manipular solicitações GET
        # Certifique-se de que há dados no banco de dados
        data = DividendoModel.objects.all()
        # Adicione um print para verificar os dados
        print("Dados recuperados:", data)
        result = [{'symbol': d.symbol, 'date': d.date, 'amount': d.amount}
                  for d in data]
        return JsonResponse(result, safe=False)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        # Lógica para manipular solicitações POST
        symbol = request.POST.get('symbol')
        date = request.POST.get('date')
        amount = request.POST.get('amount')

        if not symbol or not date or not amount:
            return HttpResponseBadRequest("Campos obrigatórios não fornecidos.")

        # Corrija para DividendoModel
        DividendoModel.objects.create(symbol=symbol, date=date, amount=amount)
        return JsonResponse({'message': 'Dividendo criado com sucesso.'})
