from django.contrib import admin
from django.urls import path
from trading.tradingEnergyApi import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('pnl/strategy/', views.Get_trades),
]
