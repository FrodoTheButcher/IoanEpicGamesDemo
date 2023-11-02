
from django.urls import path
from .views import BuyCoins,RemoveCoins

urlpatterns = [
    path('buyCoins',BuyCoins.as_view(),name="buyCoins"),
    path('removeCoins',RemoveCoins.as_view(),name="removeCoins"),
]