from .forms import BankAccountForm
from .models import Service, BankAccount
from django.shortcuts import render, redirect, get_object_or_404


def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})


def create_account(request):
    # if request.method == 'POST':
    #     form = BankAccountForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')  # Redirect to home page after successful submission
    # else:
    #     form = BankAccountForm()

    if request.method == "POST":
        full_name = request.POST['fullName']
        phone_number = request.POST['phoneNumber']
        residential_address = request.POST['residentialAddress']
        citizenship = request.POST['citizenship']
        value = BankAccount(
            full_name=full_name,
            phone_number=phone_number,
            residential_address=residential_address,
            citizenship=citizenship
        )
        value.save()
        return redirect('home')
    return render(request, 'create_account.html')


def manage_accounts(request):
    bank_accounts = BankAccount.objects.all()
    return render(request, 'manage_accounts.html', {'bank_accounts': bank_accounts})


def edit_account(request, account_id):
    account = get_object_or_404(BankAccount, id=account_id)

    if request.method == 'POST':
        form = BankAccountForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            return redirect('manage_accounts')
    else:
        form = BankAccountForm(instance=account)

    return render(request, 'edit_account.html', {'form': form, 'account': account})


def delete_account(request, account_id):
    account = get_object_or_404(BankAccount, id=account_id)

    if request.method == 'POST':
        account.delete()
        return redirect('manage_accounts')

    return render(request, 'delete_account.html', {'account': account})
