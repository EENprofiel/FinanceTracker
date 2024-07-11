from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    EXPENSE_TYPES = [
        ('one-time', 'One-time Expense'),
        ('fixed', 'Fixed Expense'),
    ]
    FREQUENCY_CHOICES = [
        ('one-time', 'One-time'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    date = models.DateField()
    expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPES, default='one-time')
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='one-time')
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        if self.expense_type == 'fixed':
            return f"{self.description} - {self.amount} (Fixed: {self.get_frequency_display()})"
        return f"{self.description} - {self.amount} (One-time)"


class Income(models.Model):
    INCOME_TYPES = [
        ('one-time', 'One-time Income'),
        ('recurring', 'Recurring Income'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=200)
    date = models.DateField()
    income_type = models.CharField(max_length=10, choices=INCOME_TYPES, default='one-time')

    def __str__(self):
        return f"{self.source} - {self.amount} ({self.get_income_type_display()})"
