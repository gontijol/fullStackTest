from django.db import models
from yahoo_fin import stock_info
from datetime import datetime


class DividendoModel(models.Model):
    symbol = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.symbol} - {self.date} - {self.amount}"


def buscar_dividendos(symbol, year):
    # Get dividend data from yahoo_fin
    dividendos = stock_info.get_dividends(symbol)

    # Filter dividend data for the given year
    dividendos_do_ano = [div for div in dividendos if datetime.strptime(
        div['Date'], '%Y-%m-%d').year == year]

    # Calculate the total dividends for the year
    total_dividendos = sum(div['Dividends'] for div in dividendos_do_ano)

    return total_dividendos
