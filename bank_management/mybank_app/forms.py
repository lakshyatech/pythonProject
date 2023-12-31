from django import forms
from .models import BankAccount


class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        exclude = []  # or specify the fields you want to include

