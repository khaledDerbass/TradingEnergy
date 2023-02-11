from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from trading.tradingEnergyApi.serializer import TradeSerializer
from django.http.response import HttpResponse
from rest_framework.response import Response
from trading.tradingEnergyApi.models import tradeModel

#def buy_sell_from_model(request):
#    data = tradeModel.objects.all()
#    response = {
#        'epex_12_20_12_13': list(data.values('side','quantity'))
#    }
#    return JsonResponse(response)

@api_view(['GET'])
def PNL_from_model(request):
    data = tradeModel.objects.all()
    response = {
        #'epex_12_20_12_13': list(data.values('id','side','strategy_id'))
       'epex_12_20_12_13': list(data.values('id','side','quantity','price','strategy_id'))

    }
    return JsonResponse(response)  

    
@api_view(['GET'])
def Get_trades (request):
    tradeData= tradeModel.objects.all()
    serialize= TradeSerializer(tradeData, many=True)
    return Response(serialize.data)
#    return JsonResponse(serialize.data)


