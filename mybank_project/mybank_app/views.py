from django.shortcuts import render, redirect
from .models import Service
from .forms import BankAccountForm


def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})


def create_account(request):
    if request.method == 'POST':
        form = BankAccountForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful submission
    else:
        form = BankAccountForm()

    return render(request, 'create_account.html', {'form': form})
