from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from .models import *
from .forms import *

def user_register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration Successful, You are logged.')
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'user_register.html', {'form': form,'page': 'Registration'})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = None
            if username_or_email and '@' in username_or_email:
                try:
                    user_obj = CustomUser.objects.get(email__iexact=username_or_email)
                    user = authenticate(
                        request, username=user_obj.username, password=password
                    )
                except CustomUser.DoesNotExist:
                    pass
            else:
                user = authenticate(
                    request, username=username_or_email, password=password
                )
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('dashboard') 
            else:
                messages.error(request, 'Invalid username/email or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {'form': form, 'page': 'Login'})

@login_required(login_url=user_login)
def change_pass(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password is successfully changed! Please login again.')
            return redirect('user_login')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'change_pass.html', {'form': form,'page': 'Change Password'})

def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('user_login')

def dashboard(request):
    user_income = AddCash.objects.filter(user=request.user)
    user_expenses = Expense.objects.filter(user=request.user)

    total_income = (
        user_income.aggregate(total=Sum('amount'))['total'] or 0
    )
    total_expense = (
        user_expenses.aggregate(total=Sum('amount'))['total'] or 0
    )
    net_balance = total_income - total_expense
    context = {
        'page': 'Dashboard',
        'total_income': total_income,
        'total_expense': total_expense,
        'net_balance': net_balance,
        'incomes': user_income.order_by('-datetime')[:5],
        'expenses': user_expenses.order_by('-datetime')[:5]
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url=user_login)
def add_cash(request):
    if request.method == 'POST':
        form = AddCashForm(request.POST)
        if form.is_valid:
            cash = form.save(commit=False)
            cash.user = request.user
            cash.save()
            messages.success(request, 'Income/Add Cash Added Successfully.')
            return redirect('dashboard')
    else:
        form = AddCashForm()
    return render(request, 'transaction_form.html', {'form': form,'title': 'Add Cash / Income','page': 'Add Cash'})

@login_required(login_url=user_login)
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid:
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense Added Successfully.')
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'transaction_form.html', {'form': form,'title': 'Add Expense','page': 'Add Expense'})