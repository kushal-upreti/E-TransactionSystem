from django.shortcuts import render
from .models import Transaction, Wallet
from .serializers import TransactionSerializers, WalletSerializers
from rest_framework import permissions, generics
from accounts.permissions import IsUserOwnerOrReadOnly
# Create your views here.

class SendMoneyView(generics.CreateAPIView):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializers

class WalletView(generics.RetrieveAPIView):
    queryset=Wallet.objects.all()
    serializer_class=WalletSerializers

class ListWallet(generics.ListAPIView):
    queryset=Wallet.objects.all()
    serializer_class=WalletSerializers
    permission_classes=[permissions.IsAdminUser]