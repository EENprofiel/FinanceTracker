from django.contrib import admin
from django.contrib.auth import login
from django.urls import include, path
from pkg_resources.extern import names

from FinanceTracker import views

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('add-income/', views.add_income, name='add_income'),
    path("accounts/", include("django.contrib.auth.urls"))
]
