# Generated by Django 4.0 on 2023-10-03 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loan_Management_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanapplication',
            name='status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loanstatus',
            name='Status',
            field=models.CharField(default=1, max_length=30),
        ),
    ]
