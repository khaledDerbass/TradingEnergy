from django.contrib import admin
from django.urls import path
from trading.tradingEnergyApi import views
from rest_framework.routers import DefaultRouter
#from rest_framework_swagger import get_swagger_view

#schema_view = get_swagger_view(title='Energy Trading API')
router = DefaultRouter()
router.register(r'pnl/strategy/', views.viewTrades.PNL_Strategy,'pnl')
router.register(r'sell/trades/', views.viewTrades.Sell_Trades,'sell')
router.register(r'buy/trades/', views.viewTrades.Buy_Trades,'buy')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('sell/trades/', views.viewTrades.Sell_Trades),

    path('buy/trades/', views.viewTrades.Buy_Trades),

    path('pnl/strategy/', views.viewTrades.PNL_Strategy),
    ]
    