from django.contrib import admin

from FinanceTracker.models import Expense, Income

# Register your models here.
admin.site.register(Expense)
admin.site.register(Income)