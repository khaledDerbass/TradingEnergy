from django.contrib import admin
from django.urls import path
from trading.tradingEnergyApi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pnl/strategy/', views.PNL_from_model,'pnl')
router.register(r'strategy/', views.Get_trades,'pnl')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('strategy/', views.Get_trades),

    path('pnl/strategy/', views.PNL_from_model),
    ]
    