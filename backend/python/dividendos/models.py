from django.db import models
from datetime import datetime
import yfinance as yf
from django.db.models import Sum


class DividendoModel(models.Model):
    symbol = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.symbol} - {self.date} - {self.amount}"

    @classmethod
    def create_dividend(cls, symbol, date, amount):
        dividend = cls(symbol=symbol, date=date, amount=amount)
        dividend.save()

    @classmethod
    def buscar_dividendos(cls, symbol, year):

        stock = yf.Ticker(symbol)
        dividends = stock.dividends

        for date, amount in dividends[dividends.index.year == year].items():
            cls.create_dividend(symbol=symbol, date=date, amount=amount)

    @classmethod
    def create_dividend(cls, symbol, date, amount):
        dividend = cls(symbol=symbol, date=date, amount=amount)
        dividend.save()

    @classmethod
    def get_dividend_summary(cls, symbol, year):
        # Consulta para obter a soma dos dividendos para o símbolo e ano fornecidos
        dividend_summary = cls.objects.filter(
            symbol=symbol, date__year=year).aggregate(total_dividend=Sum('amount'))

        # Se nenhum valor for retornado, defina o total como 0
        total_dividend = dividend_summary['total_dividend'] or 0

        return total_dividend
