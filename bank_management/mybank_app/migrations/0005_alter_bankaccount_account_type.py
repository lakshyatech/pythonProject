# Generated by Django 5.0 on 2024-01-17 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybank_app', '0004_alter_bankaccount_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_type',
            field=models.CharField(max_length=20),
        ),
    ]
