from tradingEnergyApi.models import tradeModel
from django.db.models import Sum

queryset = tradeModel.objects.all() # queryset defined as a global variable to collect all data then make data filtering 
total_sell=0
total_buy=0
class pnltrades():

    def compute_total_buy_volume(*args, **kwargs) -> float:
           totalBuy=(queryset.filter(side='buy').aggregate( total_buy=Sum('quantity'))['total_buy'])
           print('total buy is: ',total_buy)
           return totalBuy
           
    def compute_total_sell_volume(*args, **kwargs) -> float:
           totalSell=(queryset.filter(side='sell').aggregate(total_sell=Sum('quantity'))['totalSell'])
           print('total sell is: ',total_sell)

           return totalSell

    def compute_pnl(strategy_id: str, *args, **kwargs) -> float:
           pass

