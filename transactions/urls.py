from django.urls import path
from . import views

urlpatterns=[
    path('wallet_dashboard/<str:pk>', views.WalletView.as_view()),
    path('send_money/', views.SendMoneyView.as_view(), name='send-money')
]