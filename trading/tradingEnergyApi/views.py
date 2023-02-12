from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .serializer import TradeSerializer
from rest_framework.response import Response
from .models import tradeModel


queryset = tradeModel.objects.all() # queryset defined as a global variable to collect all data then make data filtering 
strategyid = ''

class viewTrades ():
    @api_view(['GET'])
    def PNL_Strategy(request):
        
        response = {
            #'epex_12_20_12_13': list(data.values('id','side','strategy_id'))
        'epex_12_20_12_13': list(queryset.values('id','side','quantity','price','strategy'))
        }
        return JsonResponse(response)  

    @api_view(['GET'])
    def Buy_Trades (request):
        tradeBuyData= queryset.filter(side='buy')
        serialize= TradeSerializer(tradeBuyData, many=True)
        strategyid= tradeBuyData.filter(strategy='strategy_id')
        return Response(serialize.data)

    @api_view(['GET'])
    def Sell_Trades (request):
        tradeSellData= queryset.filter(side='sell')
        serialize= TradeSerializer(tradeSellData, many=True)
        return Response(serialize.data)
