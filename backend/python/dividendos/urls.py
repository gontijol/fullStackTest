from django.urls import path
from .views import DividendoAPI
from .finance_data import LoadYahooFinanceData
from .filter_dividends import DividendSummaryByYearPOST

urlpatterns = [
    path('v1/', DividendoAPI.as_view(), name='dividendos-api'),
    path('v1/dividendos-petr4', LoadYahooFinanceData.as_view(),
         name='dividendos-load'),
    path('v1/filtrar-dividendos', DividendSummaryByYearPOST.as_view(),
         name='filtrar-dividendos'),
]
