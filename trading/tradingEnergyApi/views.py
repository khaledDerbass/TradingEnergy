from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from trading.tradingEnergyApi.serializer import TradeSerializer
from django.http.response import HttpResponse
from trading.tradingEnergyApi.models import tradeModel

def buy_sell_from_model(request):
    data = tradeModel.objects.all()
    response = {
        'trades': list(data.values('side','quantity'))
    }
    return JsonResponse(response)


def PNL_from_model(request):
    data = tradeModel.objects.all()
    response = {
        'trades': list(data.values('sell','quantity'))
    }
    return JsonResponse(response)  

    
@api_view(['GET'])
def Get_trades (request):
    tradeData= tradeModel.objects.all()
   #serialize= TradeSerializer(tradeData, many=True)
    serialize= TradeSerializer(tradeData)
    return HttpResponse(serialize.data)
   #return JsonResponse(serialize.data)


