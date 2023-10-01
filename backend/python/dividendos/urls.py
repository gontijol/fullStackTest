from django.urls import path
from .views import DividendoAPI
from .dividends_by_year import GetDividendsByYear
from .finance_data import LoadYahooFinanceData

urlpatterns = [
    path('v1/', DividendoAPI.as_view(), name='dividendos-api'),
    path('v1/finance-data', LoadYahooFinanceData.as_view(), name='dividendos-load'),
    path('v1/dividends-by-year/', GetDividendsByYear.as_view(),
         name='dividends-by-year'),
]
