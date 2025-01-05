from django.db import models
from django.conf import settings
from expenses.split_types import SPLIT_TYPE_CHOICES # Modified Line

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    split_type = models.CharField(max_length=50, choices=SPLIT_TYPE_CHOICES)
    date = models.DateField()
    receipt_image = models.ImageField(upload_to='receipts/', blank=True, null=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='expense_participants')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f"Expense of {self.amount} on {self.date} in {self.category}"