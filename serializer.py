from rest_framework import serializers
from DataModel import tradeModel

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
         model =  tradeModel
         fields = '__all__'