from django.shortcuts import render
from frontend.forms import BusinessForm, LoanForm

# Home page view, it loads the home page, from where all links are accessed
def HomePage(request):
    return render(request,'home_page.html')

def AddViewBusinessForm(request):
    form = BusinessForm()
    return render(request, 'business_form.html', {'form': form})

def AddViewLoanForm(request):
    form = LoanForm()
    return render(request,'loan_form.html', {'form': form})