# Generated by Django 4.0 on 2023-10-27 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loan_Management_system', '0007_alter_loanapplication_aadhaar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Acc_No',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
