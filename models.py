from datetime import date
from django.db import models

# Create your models here.
class Login(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=50)
    Type=models.CharField(max_length=50)

class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    Photo = models.CharField(max_length=500)
    First_Name=models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    Acc_No=models.CharField(max_length=100,default=1)
    IFSC=models.CharField(max_length=30,default=1)
    Gender=models.CharField(max_length=10)
    DOB=models.DateField(date(1111, 11, 11))
    Email=models.CharField(max_length=50)
    Place=models.CharField(max_length=30)
    State=models.CharField(max_length=30)
    Country=models.CharField(max_length=30)
    PIN=models.IntegerField()
    Phone=models.CharField(max_length=100)
    Status=models.CharField(max_length=20,default=1)



class LoanDetails(models.Model):
    Loan_Name = models.CharField(max_length=50)
    Amount = models.FloatField()
    Interest = models.FloatField()
    EMI = models.CharField(max_length=20)
    Loan_Duration = models.CharField(max_length=10)
    Date = models.DateField()
    Guarantee = models.CharField(max_length=30)



class LoanApplication(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    LOANDETAILS=models.ForeignKey(LoanDetails,on_delete=models.CASCADE)
    Aadhaar = models.CharField(max_length=500)
    Pan_card = models.CharField(max_length=500)
    Salary_slip = models.CharField(max_length=500)
    Guarantee = models.CharField(max_length=500,default=1)

    Status=models.CharField(max_length=100)

class LoanStatus(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    LOANAPPLICATION = models.ForeignKey(LoanApplication, on_delete=models.CASCADE)
    Status=models.CharField(max_length=30,default=1)



class EMI_History(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    LOANAPPLICATION=models.ForeignKey(LoanApplication,on_delete=models.CASCADE)
    Amount_Received=models.FloatField()
    Status=models.CharField(max_length=30)
    EMI_Pending=models.CharField(max_length=20)
    Due=models.DateField()



class Feedback(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    Date=models.DateField()
    Feedback=models.CharField(max_length=500)

class Bank(models.Model):
    Account = models.CharField(max_length=100)
    IFSC_CODE = models.CharField(max_length=100)















