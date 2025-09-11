from rest_framework import serializers
from .models import Transaction, Wallet

class WalletSerializers(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields='__all__'

class TransactionSerializers(serializers.ModelSerializer):

    class Meta:
        model=Transaction
        fields='__all__'
        read_only_fields=['status', 'timestamp', 'sender']

    def create(self, validated_data):
        validated_data['sender']=self.context['request'].user
        tx= super().create(validated_data)
        tx.approve()
        return tx