"""
Views for the frontend application, the views define the presentation of the html pages and forms required to interact with the
loan application
"""
from django.shortcuts import render
from frontend.forms import BusinessForm, LoanForm
from django.contrib.auth.decorators import login_required

# Home page view, it loads the home page, from where all links are accessed
def HomePage(request):
    return render(request,'home_page.html')

#The only page which doesn't require authentication is the home page, all the others will require it. We are adding the login_required decorator for this.

#Business Form page view, it allows the users to add a business for their loan applications
@login_required
def AddViewBusinessForm(request):
    form = BusinessForm()
    return render(request, 'business_form.html', {'form': form})

#Loan form page view, it allows the users to request a loan
@login_required
def AddViewLoanForm(request):
    form = LoanForm()
    return render(request,'loan_form.html', {'form': form})

#Final page of the process of requesting a loan view, it shows the latest request loan, previous loans and all business for the user
@login_required
def UserPage(request):
    return render(request,'user_page.html')