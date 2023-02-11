from rest_framework import serializers
from .models import tradeModel

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
         model =  tradeModel
         fields = ('id','side')