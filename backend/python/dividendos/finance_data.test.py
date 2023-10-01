from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from .models import DividendoModel
import json


class LoadYahooFinanceDataTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_load_yahoo_finance_data(self):
        # Create a dividend for the current year
        ticker = "PETR4.SA"
        year = datetime.now().year
        DividendoModel.objects.create(
            symbol=ticker, date=datetime.now(), amount=2.5)

        # Make a GET request to the view
        response = self.client.get(reverse('load_yahoo_finance_data'))

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the expected data
        expected_data = {
            'message': 'Dados carregados com sucesso.',
            'symbol': ticker,
            'dividend_date': datetime.now().strftime('%Y-%m-%d'),
            'dividend_amount': 2.5,
        }
        self.assertEqual(json.loads(response.content), expected_data)
