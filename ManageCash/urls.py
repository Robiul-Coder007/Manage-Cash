from django.urls import path
from .views import *

urlpatterns = [
    path('', user_login, name='user_login'),
    path('register/', user_register, name='user_register'),
    path('change-password/', change_pass, name='change_pass'),
    path('logout/', user_logout, name='user_logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add/cash/', add_cash, name='add_cash'),
    path('add/expense/', add_expense, name='add_expense'),
]