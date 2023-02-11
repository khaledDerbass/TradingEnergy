from rest_framework import serializers
from .models import tradeModel

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
         model =  tradeModel
         fields = '__all__'