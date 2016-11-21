from django.conf.urls import include, url
from django.contrib import admin
#Import required views from loans and frontend applications
from loans.views import AddViewBusiness, AddViewLoan
from frontend.views import HomePage, AddViewBusinessForm, AddViewLoanForm, UserPage

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^business/', AddViewBusiness.as_view(), name='business'),
    url(r'^business_form/', AddViewBusinessForm),
    url(r'^loan_form/', AddViewLoanForm),
    url(r'^loan/', AddViewLoan.as_view(), name='loan'),
    url(r'^user_page/', UserPage),
    url(r'^$', HomePage)
]
