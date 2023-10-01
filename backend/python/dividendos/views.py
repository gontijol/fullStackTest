from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import buscar_dividendos

class DividendosAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DividendosSerializer(data=request.data)
        if serializer.is_valid():
            symbol = serializer.validated_data['symbol']
            year = serializer.validated_data['year']
            total_dividendos = buscar_dividendos(symbol, year)
            return Response({'total_dividendos': total_dividendos}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
