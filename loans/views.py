from django.shortcuts import render

# Home page view, it loads the home page, from where all links are accessed
def home_page(request):
    return render(request,'home_page.html')