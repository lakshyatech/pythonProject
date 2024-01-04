from django import forms
from .models import BankAccount


class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = '__all__'


# class FilterForm(forms.Form): account_type = forms.ChoiceField(choices=[('', 'Any'), ('savings', 'Savings'),
# ('current', 'Current')], required=False) min_deposit = forms.DecimalField(label='Minimum Initial Deposit',
# required=False)
