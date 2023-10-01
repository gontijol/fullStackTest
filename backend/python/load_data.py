from dividendos.models import Dividendo
import yfinance as yf
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meu_projeto.settings")
django.setup()


def load_dividend_data():
    ticker = "PETR4.SA"
    petrobras = yf.Ticker(ticker)
    dividends = petrobras.dividends

    for date, amount in dividends.iteritems():
        Dividendo.objects.create(symbol=ticker, date=date, amount=amount)


if __name__ == "__main__":
    load_dividend_data()
