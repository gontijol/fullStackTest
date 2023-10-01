from rest_framework import serializers

class DividendosSerializer(serializers.Serializer):
    symbol = serializers.CharField(max_length=10)
    year = serializers.IntegerField()
