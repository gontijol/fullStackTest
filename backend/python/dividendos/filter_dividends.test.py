from django.test import TestCase, Client
from django.urls import reverse
import json
from .models import DividendoModel


class DividendSummaryByYearPOSTTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('dividend_summary_by_year')
        self.symbol = 'AAPL'
        self.year = 2021
        self.dividend_amount = 10.0
        DividendoModel.objects.create(
            symbol=self.symbol, date='2021-01-01', amount=self.dividend_amount)

    def test_dividend_summary_by_year_post(self):
        data = {'symbol': self.symbol, 'year': self.year}
        response = self.client.post(self.url, data=json.dumps(
            data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
                         'symbol': self.symbol, 'year': self.year, 'total_dividend': self.dividend_amount})

    def test_dividend_summary_by_year_post_missing_params(self):
        data = {'symbol': self.symbol}
        response = self.client.post(self.url, data=json.dumps(
            data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
                         'error': 'Parâmetros de símbolo e ano são obrigatórios.'})

    def test_dividend_summary_by_year_post_invalid_params(self):
        data = {'symbol': self.symbol, 'year': 'invalid_year'}
        response = self.client.post(self.url, data=json.dumps(
            data), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertIn('invalid literal for int() with base 10',
                      response.json()['error'])
