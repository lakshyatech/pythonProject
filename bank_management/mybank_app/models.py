from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    id_proof = models.CharField(max_length=20)
    account_type = models.CharField(max_length=10, choices=[('savings', 'Savings Account'), ('current', 'Current Account')])
    email_address = models.EmailField()
    date_of_birth = models.DateField()
    residential_address = models.TextField()
    # digital_picture = models.ImageField(upload_to='digital_pictures/')
    citizenship = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    agree_t_and_c = models.BooleanField()

    def __str__(self):
        return self.full_name
