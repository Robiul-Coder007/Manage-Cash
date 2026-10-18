from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Input Username"}))
    display_name = forms.CharField(label="Display Name", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Input Display Name"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Input Email"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Input Password"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Input Confirm Password"}))

    class Meta:
        model = CustomUser
        fields = ["username","display_name","email","password1","password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email",widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Input Username or Email"}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Input Password"}))

    class Meta:
        model = CustomUser
        fields = ["username","password"]

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password",widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Input Old Password"}))
    new_password1 = forms.CharField(label="New Password",widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Input New Password"}))
    new_password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Input Confirm Password"}))

    class Meta:
        model = CustomUser
        fields = ["old_password","new_password1","new_password2"]

class AddCashForm(forms.ModelForm):
    source = forms.CharField(label="Source",widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Input Source (e.g. Salary, Business)"}))
    amount = forms.IntegerField(label="Amount",widget=forms.NumberInput(attrs={"class": "form-control","placeholder": "Input Amount"}))
    description = forms.CharField(label="Description",required=False,widget=forms.Textarea(attrs={"class": "form-control","rows": 3,"placeholder": "Input Description"}))

    class Meta:
        model = AddCash
        fields = ["source","amount","description"]

class ExpenseForm(forms.ModelForm):
    amount = forms.IntegerField(label="Amount",widget=forms.NumberInput(attrs={"class": "form-control","placeholder": "Input Amount"}))
    description = forms.CharField(label="Description",required=False,widget=forms.Textarea(attrs={"class": "form-control","rows": 3,"placeholder": "Input Description"}))

    class Meta:
        model = Expense
        fields = ["amount","description"]