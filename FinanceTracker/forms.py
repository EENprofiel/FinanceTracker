from django import forms
from .models import Expense, Income


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'description', 'date', 'expense_type', 'frequency', 'end_date']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'source', 'date', 'income_type']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
