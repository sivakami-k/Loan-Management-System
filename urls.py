"""
URL configuration for untitled project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Loan_Management_system import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('adminhome/', views.adminhome),
    path('forget_password/', views.forget_password),
    path('admin_add_loan/', views.adminld),
    path('admin_view_applications/', views.adminmla),
    path('approve_loan/<id>/', views.approve_loan),
    path('reject_loan/<id>/', views.reject_loan),
    path('admin_view_pending_registration/', views.view_user),
    path('approve_user/<id>/', views.approve_user),
    path('reject_user/<id>/', views.reject_user),
    path('admin_upload_emi/<id>/', views.adminueh),
    path('edit_emi/<id>/', views.edit_emi),
    path('admin_delete_emihistory/<id>/', views.admin_delete_emihistory),
    path('admin_upload_loan_status/<id>/', views.adminuls),
    path('viewloan_status/', views.viewloan_status),
    path('admin_view_approved_loan/', views.adminvala),
    path('admin_view_approved_users/', views.adminvau),
    path('admin_view_rejected_loan/', views.adminvrla),
    path('admin_view_rejected_users/', views.adminvru),
    path('admin_update_loan_application/', views.adminvula),
    path('admin_view_loandetails/', views.admin_view_loandetails),
    path('admin_view_emi/', views.admin_view_emi),
    path('admin_edit_loandetails/<id>/', views.admin_edit_loandetails),
    path('admin_delete_loandetails/<id>/', views.admin_delete_loandetails),
    path('assign_emi/<id>/', views.admin_delete_loandetails),
    path('viewfeedback/', views.viewfeedback),


    path('login_post/', views.login_post),
    path('forgot_pass_post/', views.forgot_pass_post),
    path('loandetails_post/', views.loandetails_post),
    path('manageloan_post/', views.manageloan_post),
    path('manageregistration_post/', views.manageregistration_post),
    path('uploademi_post/', views.uploademi_post),
    path('editemi_post/', views.editemi_post),
    # path('updateloanstatus_post/', views.updateloanstatus_post),
    path('viewloan_status_post/', views.viewloan_status_post),
    path('viewapprovedloan_post/', views.viewapprovedloan_post),
    path('viewapproveduser_post/', views.viewapproveduser_post),
    path('viewrejectedloan_post/', views.viewrejectedloan_post),
    path('viewrejecteduser_post/', views.viewrejecteduser_post),
    path('updateloanstatus_post/', views.updateloanstatus_post),
    path('viewloandetails_post/', views.viewloandetails_post),
    path('viewemi_post/', views.viewemi_post),
    path('editloan_post/', views.editloan_post),
    path('viewfeedbackpost/', views.viewfeedbackpost),

    ##########33user




    path('userhome/', views.userhome),
    path('apply_loan/<id>', views.apply_loan),
    path('edit_loanapplication/<did>', views.edit_loanapplication),
    path('delete_application/<id>', views.delete_application),
    path('edit_profile/', views.edit_profile),
    path('registration/', views.registration),
    path('view_emi_details/', views.view_emi_details),
    path('view_loan_details/', views.view_loan_details),
    path('view_loan_status/', views.view_loan_status),
    path('view_profile/', views.view_profile),
    path('view_loanapplication/', views.view_loanapplication),
    path('sendfeedback/', views.sendfeedback),

    path('applyloan_post/', views.applyloan_post),
    path('editapplication_post/', views.editapplication_post),
    path('editprofile_post/', views.editprofile_post),
    path('registration_post/', views.registration_post),
    path('view_emi_post/', views.view_emi_post),
    path('view_loandetails_post1/', views.view_loandetails_post1),
    path('viewloanstatus_post/', views.viewloanstatus_post),
    path('viewapplication_post/', views.viewapplication_post),
    path('feedbackpost/', views.feedbackpost),

]
