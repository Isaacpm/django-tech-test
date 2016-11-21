from django.shortcuts import render
from frontend.forms import BusinessForm, LoanForm
from django.contrib.auth.decorators import login_required

# Home page view, it loads the home page, from where all links are accessed
def HomePage(request):
    return render(request,'home_page.html')

@login_required
def AddViewBusinessForm(request):
    form = BusinessForm()
    return render(request, 'business_form.html', {'form': form})

@login_required
def AddViewLoanForm(request):
    form = LoanForm()
    return render(request,'loan_form.html', {'form': form})

@login_required
def UserPage(request):
    return render(request,'user_page.html')