from .forms import BankAccountForm
from .models import Service, BankAccount
from django.shortcuts import render, redirect, get_object_or_404


def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})


def create_account(request):
    if request.method == "POST":
        full_name = request.POST['fullName']
        phone_number = request.POST['phoneNumber']
        id_proof = request.POST['idProof']
        account_type = request.POST['accountType']
        email_address = request.POST['emailAddress']
        date_of_birth = request.POST['dateOfBirth']
        residential_address = request.POST['residentialAddress']
        # digital_picture = request.FILES['digitalPicture']
        citizenship = request.POST['citizenship']
        initial_deposit = request.POST['initialDeposit']
        agree_t_and_c = request.POST.get('agreeTAndC', False)
        if agree_t_and_c == ['on']:
            agree_t_and_c = True
        else:
            agree_t_and_c = False
        # Create a new BankAccount object
        new_account = BankAccount(
            full_name=full_name,
            phone_number=phone_number,
            id_proof=id_proof,
            account_type=account_type,
            email_address=email_address,
            date_of_birth=date_of_birth,
            residential_address=residential_address,
            # digital_picture=digital_picture,
            citizenship=citizenship,
            initial_deposit=initial_deposit,
            agree_t_and_c=agree_t_and_c
        )
        new_account.save()
        return redirect('home')
    return render(request, 'create_account.html')


def manage_accounts(request):
    if request.method == "POST":
        account_type = request.POST['accountType']
        accounts = BankAccount.objects.filter(account_type=account_type)
    else:
        accounts = BankAccount.objects.all()
    return render(request, 'manage_accounts.html', {'bank_accounts': accounts})


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
