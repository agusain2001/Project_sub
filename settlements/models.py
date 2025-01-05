from django.db import models
from django.conf import settings
from settlements.settlement_choices import PAYMENT_STATUS_CHOICES  # Modified Line


class Settlement(models.Model):
    payer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='payer_settlements', on_delete=models.CASCADE)
    payee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='payee_settlements', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES) # pending, completed
    settlement_method = models.CharField(max_length=50, blank=True, null=True)  # UPI, Cash, etc
    due_date = models.DateField(blank=True, null=True)
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Settlement from {self.payer} to {self.payee} due on {self.due_date}"