from django.db import models
from yahoo_fin import stock_info


class Dividendo(models.Model):
    symbol = models.CharField(max_length=255)
    # Você pode definir um valor padrão aqui
    date = models.DateField(default=None)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.symbol} - {self.date} - {self.amount}"


def buscar_dividendos(symbol, year):
    dividendos = stock_info.get_dividends(symbol)
    dividendos_do_ano = [div for div in dividendos if div['Date'].year == year]
    total_dividendos = sum(div['Dividends'] for div in dividendos_do_ano)
    return total_dividendos
