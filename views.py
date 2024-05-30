import datetime
import string

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.db import IntegrityError
from Loan_Management_system.models import *
# Create your views here.
def login(request):
    return render(request,"indexlogin.html")

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    if Login.objects.filter(Username=username,Password=password).exists():
        obj=Login.objects.get(Username=username,Password=password)
        request.session["lid"]=obj.id
        if obj.Type=="admin":
            return render(request, "admin/adminindex.html")
        elif obj.Type=="user":
            if User.objects.get(LOGIN_id=obj.id).Status=='Pending':
                return HttpResponse("<script>alert('Not Approved');window.location='/Myapp/login/'</script>")

            return render(request,"user/userindex.html")
        else:
            return HttpResponse("<script>alert('Invalid username or password');window.location='/Myapp/login/'</script>")
    else:
        return HttpResponse("<script>alert('Invalid username or password');window.location='/Myapp/login/'</script>")


def forget_password(request):
    return render(request, 'admin/forgetpassword.html')

def forgot_pass_post(request):
    em = request.POST['textfield']
    import random
    ch=string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choice(ch)for i in range(8))
    log=Login.objects.filter(Username=em)
    if log.exists():
        logg = Login.objects.get(Username=em)
        message = 'new password is ' + str(password)
        send_mail(
            ' password',
            message,
            settings.EMAIL_HOST_USER,
            [em, ],
            fail_silently=False
        )
        logg.Password=password
        logg.save()
        return HttpResponse('<script>alert("success");window.location="/Myapp/login/"</script>')
    else:
        return HttpResponse('<script>alert("invalid email");window.location="/Myapp/login/"</script>')

def logout(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    request.session['lid']=''
    return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")


def adminhome(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    return render(request,"admin/adminindex.html")

def adminld(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")

    return render(request,"admin/Admin_loan_details.html")

def loandetails_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    loanname=request.POST['textfield']
    loanamount=request.POST['textfield2']
    interest=request.POST['textfield3']
    emi=request.POST['textfield4']
    loanduration=request.POST['textfield7']
    date=request.POST['textfield5']
    guarantee=request.POST['textfield6']


    obj=LoanDetails()
    obj.Loan_Name=loanname
    obj.Amount=loanamount
    obj.Interest=interest
    obj.EMI=emi
    obj.Loan_Duration=loanduration
    obj.Date=date
    obj.Guarantee=guarantee
    obj.save()
    return HttpResponse('''<script>alert('Upload successful');window.location="/Myapp/admin_view_loandetails/"</script>''')


def adminmla(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=LoanApplication.objects.filter(Status='Pending')
    return render(request,"admin/Admin_manage_loanapplication.html",{'data':res})

def manageloan_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    search=request.POST['textfield']
    res=LoanApplication.objects.filter(USER__Acc_No=search,Status='Pending')

    return render(request,"admin/Admin_manage_loanapplication.html",{'data':res})

def approve_loan(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=LoanApplication.objects.filter(id=id).update(Status="Approved")
    return HttpResponse('''<script>alert('Approved');window.location="/Myapp/admin_view_approved_loan/"</script>''')

def reject_loan(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=LoanApplication.objects.filter(id=id).update(Status="Rejected")
    return HttpResponse('''<script>alert('Rejected');window.location="/Myapp/admin_view_rejected_loan/"</script>''')



def view_user(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=User.objects.filter(Status='Pending')
    return render(request,"admin/Admin_Manage_registrations.html",{'data':res})

def manageregistration_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    search=request.POST['textfield']
    res=User.objects.filter(Acc_No=search,Status='Pending')

    return render(request,"admin/Admin_Manage_registrations.html",{'data':res})

def approve_user(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=User.objects.filter(LOGIN_id=id).update(Status="Approved")
    res=Login.objects.filter(pk=id).update(Type="user")

    return HttpResponse('''<script>alert('Approved');window.location="/Myapp/admin_view_approved_users/"</script>''')

def reject_user(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res = User.objects.filter(id=id).update(Status="Rejected")
    res=Login.objects.filter(pk=id).update(Type="Rejected")
    return HttpResponse('''<script>alert('Rejected');window.location="/Myapp/admin_view_rejected_users/"</script>''')

def assign_emi(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")

    res=EMI_History.objects.get(id=id)

    return HttpResponse("ok")

def adminueh(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=LoanApplication.objects.get(id=id)
    dt= datetime.date.today()
    return render(request,"admin/Admin_upload_EMI_history.html",{'id':res,'dt':str(dt)})

def uploademi_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    id=request.POST['id']
    # loanname = request.POST['id']
    # print(loanname,"hai")
    amountreceived = request.POST['textfield2']
    status = request.POST['select2']
    emipending = request.POST['textfield4']
    due = request.POST['textfield5']
    obj=EMI_History()
    # obj=EMI_History.objects.get(LOANAPPLICATION_id=id)
    obj.LOANAPPLICATION_id=id
    obj.Amount_Received=amountreceived
    obj.Status=status
    obj.Due=due
    obj.EMI_Pending=emipending
    obj.USER_id=LoanApplication.objects.get(id=id).USER_id
    obj.save()
    # obj=EMI_History.objects.get(id=id)
    # obj.LOANAPPLICATION=LoanApplication.objects.get(id=loanname)
    # obj.Amount_Received=amountreceived
    # obj.Status=status
    # obj.EMI_Pending=emipending
    # obj.Due=due
    # obj.save()
    return HttpResponse('''<script>alert('Upload successful');window.location="/Myapp/admin_view_approved_loan/"</script>''')


def adminuls(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=LoanApplication.objects.filter(id=id)
    return render(request,"admin/Admin_upload_loan_status.html")

def updateloanstatus_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=request.POST['RadioGroup1']
    obj=LoanApplication()
    obj.Status=res
    obj.save()


    return HttpResponse('''<script>alert('Upload successfull');window.location="'/Myapp/admin_view_approved_loan/"</script>''')

def adminvala(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res = LoanApplication.objects.filter(Status='Approved')
    return render(request,"admin/Admin_view_approved_loanapplication.html",{'data':res})

def viewapprovedloan_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    search = request.POST['textfield']
    res=LoanApplication.objects.filter(Status='Approved',USER__Acc_No=search)

    return render(request,"admin/Admin_view_approved_loanapplication.html",{'data':res})

def adminvau(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res = User.objects.filter(Status='Approved')
    return render(request,"admin/Admin_view_approved_users.html",{'data':res})

def viewapproveduser_post(request):
    search = request.POST['textfield']
    res=User.objects.filter(Status='Approved',Acc_No=search)

    return render(request,"admin/Admin_view_approved_users.html",{'data':res})

def adminvrla(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logging out');window.location='/Myapp/login/'</script>")
    res = LoanApplication.objects.filter(Status='Rejected')
    return render(request,"admin/Admin_view_rejected_loanapplication.html",{'data':res})

def viewrejectedloan_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    search = request.POST['textfield']
    res=LoanApplication.objects.filter(Status='Rejected',USER__Acc_No=search)

    return render(request,"admin/Admin_view_rejected_loanapplication.html",{'data':res})

def adminvru(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res = User.objects.filter(Status='Rejected')
    return render(request,"admin/Admin_view_rejected_users.html",{'data':res})

def viewrejecteduser_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    search = request.POST['textfield']
    res=User.objects.filter(Status='Rejected',Acc_No__icontains=search)

    return render(request,"admin/Admin_view_rejected_users.html",{'data':res})


def adminvula(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res = LoanApplication.objects.all()
    return render(request,"admin/Admin_viewandupdate_loanapp.html",{'data':res})

# def updateloanstatus_post(request):
#     search = request.POST['textfield']
#
#     return HttpResponse("ok")

def viewloan_status(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=LoanStatus.objects.all()
    return render(request,"admin/Admin_view_loan_status.html",{'data':res})


def viewloan_status_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    search = request.POST['textfield']
    return HttpResponse("ok")


def admin_view_loandetails(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    obj=LoanDetails.objects.all()
    return render(request,"admin/Admin_view_update_loandetails.html",{'data':obj})

def viewloandetails_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")

    search = request.POST['textfield']
    obj=LoanDetails.objects.filter(Loan_Name=search)

    return render(request,"admin/Admin_view_update_loandetails.html",{'data':obj})

def admin_view_emi(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res = EMI_History.objects.all()
    return render(request,"admin/Admin_view_update_emi.html",{'data':res})

def viewemi_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    search = request.POST['textfield']

    res=EMI_History.objects.filter(Status=search)

    return render(request,"admin/Admin_view_update_emi.html",{'data':res})

def edit_emi(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=EMI_History.objects.get(id=id)
    dt = datetime.date.today()
    return render(request,"admin/Admin_edit_EMI_history.html",{'data':res,'dt':str(dt)})

def editemi_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    id=request.POST['id']

    # name=request.POST['textfield']
    # loanname = request.POST['select']
    amountreceived = request.POST['textfield2']
    status = request.POST['select2']
    emipending = request.POST['textfield4']
    due = request.POST['textfield5']


    obj = EMI_History.objects.filter(id=id).update(Amount_Received=amountreceived,Status=status,EMI_Pending=emipending,Due=due)


    # obj = EMI_History.objects.get(id=id)
    # # obj.USER = User.objects.get(id=name)
    # # obj.LOANAPPLICATION = LoanApplication.objects.get(id=loanname)
    # obj.Amount_Received = amountreceived
    # obj.Status = status
    # obj.EMI_Pending = emipending
    # obj.Due = due
    # obj.save()
    return HttpResponse('''<script>alert('Upload successful');window.location="/Myapp/admin_view_emi/"</script>''')


def admin_delete_emihistory(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res = EMI_History.objects.get(id=id)
    res.delete()
    return HttpResponse('''<script>alert('EMI History deleted');window.location='/Myapp/admin_view_emi/'</script>''')


def admin_edit_loandetails(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=LoanDetails.objects.get(id=id)

    return render(request,"admin/Admin_edit_loan_details.html",{'data':res})

def editloan_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    id=request.POST['id']
    loanname = request.POST['textfield']
    loanamount = request.POST['textfield2']
    interest = request.POST['textfield3']
    emi = request.POST['textfield4']
    loanduration = request.POST['textfield7']
    date = request.POST['textfield5']
    guarantee = request.POST['textfield6']

    obj = LoanDetails.objects.get(id=id)
    obj.Loan_Name = loanname
    obj.Amount = loanamount
    obj.Interest = interest
    obj.EMI = emi
    obj.Loan_Duration = loanduration
    obj.Date = date
    obj.Guarantee = guarantee
    obj.save()

    return HttpResponse('''<script>alert('Loan datails updated');window.location='/Myapp/admin_view_loandetails/'</script>''')


def admin_delete_loandetails(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=LoanDetails.objects.get(id=id)
    res.delete()
    return HttpResponse('''<script>alert('Loan datails deleted');window.location='/Myapp/admin_view_loandetails/'</script>''')

def viewfeedback(request):
    fobj=Feedback.objects.all()
    return render(request,'admin/Admin_view_feedback.html',{"data":fobj})

def viewfeedbackpost(request):
    fromdate=request.POST['textfield1']
    todate=request.POST['textfield2']
    fobj=Feedback.objects.filter(Date__range=[fromdate,todate])
    return render(request,'admin/Admin_view_feedback.html',{"data":fobj})

##################################user

def userhome(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    return render(request,"user/userindex.html")


def apply_loan(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")

    return render(request,"user/User_apply_loan.html",{'id':id})

def applyloan_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    did=request.POST['id1']
    aadhaar = request.FILES['fileField2']
    fs1 = FileSystemStorage()
    from datetime import datetime

    da1 = "aadhaar/" + datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    fn1 = fs1.save(da1, aadhaar)

    pancard = request.FILES['fileField3']
    fs2 = FileSystemStorage()
    from datetime import datetime

    da2 = "pancard/" + datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    fn2 = fs2.save(da2, pancard)

    salaryslip = request.FILES['fileField4']
    fs3 = FileSystemStorage()
    from datetime import datetime

    da3 = "salaryslip/" + datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    fn3 = fs3.save(da3, salaryslip)

    guarantee = request.FILES['fileField5']
    fs4 = FileSystemStorage()
    from datetime import datetime

    da4 = "guarantee/" + datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    fn4 = fs4.save(da4, guarantee)



    obj=LoanApplication()
    obj.Aadhaar=fs1.url(fn1)
    obj.Pan_card=fs2.url(fn2)
    obj.Salary_slip=fs3.url(fn3)
    obj.Guarantee=fs4.url(fn4)
    lid=User.objects.get(LOGIN=request.session['lid'])
    obj.USER_id=lid.id
    obj.Status='Pending'

    obj.LOANDETAILS_id=did

    obj.save()


    return HttpResponse('''<script>alert('Upload successful');window.location="/Myapp/view_loanapplication/"</script>''')

def edit_loanapplication(request,did):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=LoanApplication.objects.get(id=did)
    return render(request,"user/User_view_loanapplication.html",{'data':res})

def editapplication_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    did = request.POST['id1']
    obj = LoanApplication.objects.get(id=did)

    if 'fileField2' in request.FILES:
        aadhaar = request.FILES['fileField2']
        if aadhaar.name!='':
            fs1 = FileSystemStorage()
            from datetime import datetime

            da1 = "aadhaar/" + datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
            fn1 = fs1.save(da1, aadhaar)
            obj.Aadhaar = fs1.url(fn1)

    if 'fileField3' in request.FILES:
        pancard = request.FILES['fileField3']
        if pancard.name!='':
            fs2 = FileSystemStorage()
            from datetime import datetime

            da2 = "pancard/" + datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
            fn2 = fs2.save(da2, pancard)
            obj.Pan_card = fs2.url(fn2)

    if 'fileField4' in request.FILES:
        salaryslip = request.FILES['fileField4']
        if salaryslip.name!='':
            fs3 = FileSystemStorage()
            from datetime import datetime

            da3 = "salaryslip/" + datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
            fn3 = fs3.save(da3, salaryslip)
            obj.Salary_slip = fs3.url(fn3)

    if 'fileField5' in request.FILES:
        guarantee = request.FILES['fileField5']
        if guarantee.name!='':
            fs4 = FileSystemStorage()
            from datetime import datetime

            da4 = "guarantee/" + datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
            fn4 = fs4.save(da4, guarantee)
            obj.Guarantee = fs4.url(fn4)

    # lid = User.objects.get(LOGIN=request.session['lid'])
    # obj.USER_id = lid.id
    #
    # obj.LOANDETAILS_id = did

    obj.save()

    return HttpResponse('''<script>alert('Upload successful');window.location="/Myapp/view_loanapplication/"</script>''')


def delete_application(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res = LoanApplication.objects.get(id=id)
    res.delete()
    return HttpResponse('''<script>alert('Loan Application cancelled');window.location='/Myapp/view_loanapplication/'</script>''')


def edit_profile(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=User.objects.get(LOGIN=request.session['lid'])
    return render(request,"user/User_edit_profile.html",{'data':res})

def editprofile_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    firstname = request.POST['textfield']
    lastname = request.POST['textfield2']
    # accno = request.POST['textfield12']
    # ifsc = request.POST['textfield13']
    #
    # gender = request.POST['RadioGroup1']
    # dob = request.POST['textfield11']
    email = request.POST['textfield3']
    place = request.POST['textfield4']
    state = request.POST['textfield5']
    country = request.POST['textfield6']
    pin = request.POST['textfield7']
    phone = request.POST['phone']

    obj = User.objects.get(LOGIN=request.session['lid'])
    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']
        if photo !="":
            from datetime import datetime
            fs = FileSystemStorage()

            da = "user/" + datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
            fn = fs.save(da, photo)

            obj.Photo = fs.url(da)
    obj.First_Name = firstname
    obj.Last_Name = lastname
    # obj.Acc_No = accno
    # obj.IFSC = ifsc
    #
    # obj.Gender = gender
    # obj.DOB = dob
    obj.Email = email
    obj.Place = place
    obj.State = state
    obj.Country = country
    obj.PIN = pin
    obj.Phone = phone
    obj.save()

    return HttpResponse("<script>alert('Successfully updated');window.location='/Myapp/view_profile/'</script>")



def registration(request):
    return render(request,"user/signup_index.html")

# def registration_post(request):
#     photo = request.FILES['fileField']
#
#     firstname = request.POST['textfield']
#     lastname = request.POST['textfield2']
#     accno = request.POST['textfield12']
#     ifsc = request.POST['textfield13']
#
#     gender = request.POST['RadioGroup1']
#     dob = request.POST['textfield11']
#     email = request.POST['textfield3']
#     place = request.POST['textfield4']
#     state = request.POST['textfield5']
#     country = request.POST['textfield6']
#     pin = request.POST['textfield7']
#     phone = request.POST['textfield8']
#     password = request.POST['textfield9']
#     confirmpassword = request.POST['textfield10']
#
#     try:
#         if Bank.objects.filter(Account=accno, IFSC_CODE=ifsc).exists():
#             if password == confirmpassword:
#                 fs = FileSystemStorage()
#                 from datetime import datetime
#                 da = "user/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
#                 fn = fs.save(da, photo)
#
#                 obj1 = Login()
#                 obj1.Username = email
#                 obj1.Password = password
#                 obj1.Type = "Pending"
#                 obj1.save()
#
#                 obj = User()
#                 obj.Photo = fs.url(fn)
#                 obj.First_Name = firstname
#                 obj.Last_Name = lastname
#                 obj.Acc_No = accno
#                 obj.IFSC = ifsc
#
#                 obj.Gender = gender
#                 obj.DOB = dob
#                 obj.Email = email
#                 obj.Place = place
#                 obj.State = state
#                 obj.Country = country
#                 obj.PIN = pin
#                 obj.Phone = phone
#                 obj.LOGIN = obj1
#                 obj.Status = 'Pending'
#                 obj.save()
#
#                 return HttpResponse("<script>alert('Registration Successful');window.location='/Myapp/registration'</script>")
#             else:
#                 return HttpResponse("<script>alert('Confirm password does not match with password');window.location='/Myapp/registration'</script>")
#         else:
#             return HttpResponse("<script>alert('Account Number or IFSC CODE does not match');window.location='/Myapp/registration'</script>")
#     except IntegrityError as e:
#         if 'unique constraint' in str(e).lower():
#             return HttpResponse("<script>alert('Email address is already registered. Please use a different email.');window.location='/Myapp/registration'</script>")
#         else:
#             return HttpResponse("<script>alert('Email address is already registered. Please use a different email.);window.location='/Myapp/registration'</script>")
def registration_post(request):
    photo = request.FILES['fileField']

    firstname = request.POST['textfield']
    lastname = request.POST['textfield2']
    accno = request.POST['textfield12']
    ifsc = request.POST['textfield13']

    gender = request.POST['RadioGroup1']
    dob=request.POST['textfield11']
    email = request.POST['textfield3']
    place = request.POST['textfield4']
    state = request.POST['textfield5']
    country = request.POST['textfield6']
    pin = request.POST['textfield7']
    phone = request.POST['textfield8']
    password = request.POST['textfield9']
    confirmpassword = request.POST['textfield10']
    if Bank.objects.filter(Account=accno,IFSC_CODE=ifsc).exists():
        if password==confirmpassword:

            fs=FileSystemStorage()
            from datetime import datetime

            da="user/"+datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
            fn=fs.save(da,photo)

            obj1=Login()
            obj1.Username=email
            obj1.Password=password
            obj1.Type="Pending"
            obj1.save()
            obj=User()
            obj.Photo=fs.url(fn)
            obj.First_Name=firstname
            obj.Last_Name=lastname
            obj.Acc_No=accno
            obj.IFSC=ifsc

            obj.Gender=gender
            obj.DOB=dob
            obj.Email=email
            obj.Place=place
            obj.State=state
            obj.Country=country
            obj.PIN=pin
            obj.Phone=phone
            obj.LOGIN=obj1
            obj.Status='Pending'
            obj.save()

            return HttpResponse("<script>alert('Registration Successful');window.location='/Myapp/registration'</script>")
        else:
            return HttpResponse("<script>alert('Confirm password doesnot match with password');window.location='/Myapp/registration'</script>")
    else:
        return HttpResponse("<script>alert('Account Number or IFSC CODE does not match');window.location='/Myapp/registration'</script>")

def view_emi_details(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=EMI_History.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,"user/User_view_emi_details.html",{'data':res})


def view_emi_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    search = request.POST['textfield']
    res = EMI_History.objects.filter(Status=search)

    return render(request,"user/User_view_emi_details.html",{'data': res})



def view_loan_details(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    obj = LoanDetails.objects.all()
    return render(request,"user/User_view_loan_details.html",{'data':obj})


def view_loandetails_post1(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    search = request.POST['textfield']
    obj=LoanDetails.objects.filter(Loan_Name=search)

    return render(request,"user/User_view_loan_details.html",{'data':obj})

def view_loan_status(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=LoanApplication.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,"user/User_view_loan_status.html",{'data':res})


def viewloanstatus_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    search = request.POST['textfield']
    res=LoanApplication.objects.filter(USER__LOGIN_id=request.session['lid'],LOANDETAILS__Loan_Name=search)
    # res = LoanStatus.objects.filter(USER__LOGIN_id=request.session['lid'],LOANAPPLICATION__LOANDETAILS__Loan_Name=search)

    return render(request,"user/User_view_loan_status.html",{'data':res})

def view_profile(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"user/User_view_profile.html",{'data':res})


def viewprofile_posadmin_upload_emit(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    search = request.POST['textfield']

    return HttpResponse("ok")

def view_loanapplication(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    res=LoanApplication.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,"user/User_view_application.html",{'data':res})

def viewapplication_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Logged out');window.location='/Myapp/login/'</script>")
    search = request.POST['textfield']
    res = LoanApplication.objects.filter(LOANDETAILS__Loan_Name=search,USER__LOGIN_id=request.session['lid'])

    return render(request, "user/User_view_application.html", {'data': res})


def sendfeedback(request):
    return render(request,'user/User_send_feedback.html')

def feedbackpost(request):
    feedback=request.POST['feed']
    fobj=Feedback()
    fobj.Feedback=feedback
    fobj.USER=User.objects.get(LOGIN=request.session['lid'])
    import datetime
    date=datetime.datetime.now().date()
    fobj.Date=date
    fobj.save()
    return HttpResponse("<script>alert('Feedback Sent');window.location='/Myapp/userhome/'</script>")



def show(request):
    return