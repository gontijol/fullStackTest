from django.urls import path
from .views import DividendosAPI

urlpatterns = [
    path('v1/', DividendosAPI.as_view(), name='dividendos-api'),
]
