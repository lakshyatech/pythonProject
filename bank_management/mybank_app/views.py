from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import BankAccount
from .forms import BankAccountForm
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


class BankAccountListView(ListView):
    model = BankAccount
    template_name = 'manage_accounts.html'
    context_object_name = 'bank_accounts'


class BankAccountCreateView(CreateView):
    model = BankAccount
    form_class = BankAccountForm
    template_name = 'create_account.html'
    success_url = reverse_lazy('home')


class BankAccountUpdateView(UpdateView):
    model = BankAccount
    form_class = BankAccountForm
    template_name = 'edit_account.html'
    success_url = reverse_lazy('manage_accounts')


class BankAccountDeleteView(DeleteView):
    model = BankAccount
    template_name = 'delete_account.html'
    success_url = reverse_lazy('manage_accounts')
