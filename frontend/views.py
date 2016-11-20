from django.shortcuts import render

# Home page view, it loads the home page, from where all links are accessed
def HomePage(request):
    return render(request,'home_page.html')

def AddViewBusinessForm(request):
    return render(request,'business_form.html')

def AddViewLoanForm(request):
    return render(request,'loan_form.html')