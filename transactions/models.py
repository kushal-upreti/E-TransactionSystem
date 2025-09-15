from django.db import models
from accounts.models import UserProfile
from decimal import Decimal
# Create your models here.
class Wallet(models.Model):
    user=models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True)
    balance=models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))

    def debit(self, amount):
        if self.balance < amount:
            raise ValueError('Insufficient Balance')
        self.balance -=amount
        self.save(update_fields=['balance'])

    def credit(self, amount):
        self.balance += amount
        self.save(update_fields=['balance'])

    def __str__(self):
        return self.user.name

class Transaction(models.Model):
    sender=models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver=models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_transactions')
    amount= models.DecimalField(max_digits=12, decimal_places=2)
    status=models.CharField(max_length=20, choices=[('pending', "Pending"),('success', 'Success'), ('rejected', 'Rejected')], default='pending')
    timestamp=models.DateTimeField(auto_now_add=True)

    def approve(self):
        from django.db import transaction as db_transaction
        if self.status != 'pending':
            raise ValueError('Transaction already processed')
        with db_transaction.atomic():

            try:
                sender_wallet= Wallet.objects.select_for_update().get(user=self.sender)
                receiver_wallet= Wallet.objects.select_for_update().get(user=self.receiver)
            except Wallet.DoesNotExist:
                raise ValueError("Wallet Doesnot exist for that user:")
            
            sender_wallet.debit(self.amount)
            receiver_wallet.credit(self.amount)
            
            self.status= 'success'
            self.save(update_fields=['status'])
    
    