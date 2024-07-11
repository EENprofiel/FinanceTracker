from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from .models import Expense, Income
from .forms import ExpenseForm, IncomeForm


@login_required
def dashboard(request):
    current_month = timezone.now().month
    current_year = timezone.now().year
    expenses = Expense.objects.filter(user=request.user, date__month=current_month, date__year=current_year)
    incomes = Income.objects.filter(user=request.user, date__month=current_month, date__year=current_year)
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    total_income = incomes.aggregate(Sum('amount'))['amount__sum'] or 0

    # Prepare data for the pie chart
    chart_data = {
        'labels': ['Expenses', 'Income'],
        'data': [float(total_expense), float(total_income)]  # Convert to float
    }

    # Separate one-time and fixed expenses
    one_time_expenses = expenses.filter(expense_type='one-time')
    fixed_expenses = expenses.filter(expense_type='fixed')

    context = {
        'one_time_expenses': one_time_expenses,
        'fixed_expenses': fixed_expenses,
        'incomes': incomes,
        'total_expense': total_expense,
        'total_income': total_income,
        'chart_data': chart_data,
    }
    return render(request, 'FinanceTracker/dashboard.html', context)


@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error adding expense. Please check the form.')
    else:
        form = ExpenseForm()
    return render(request, 'FinanceTracker/add_expense.html', {'form': form})


@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            messages.success(request, 'Income added successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error adding income. Please check the form.')
    else:
        form = IncomeForm()
    return render(request, 'FinanceTracker/add_income.html', {'form': form})
