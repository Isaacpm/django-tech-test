"""
URLs for the Grothw Street project.
We keep them all in this file as the url handling is quite basic.
If the url patterns grow, they should be split in different files, using the applications' url files.
"""
from django.conf.urls import include, url
from django.contrib import admin
#Import required views from loans and frontend applications
from loans.views import AddViewBusiness, AddViewLoan
from frontend.views import HomePage, AddViewBusinessForm, AddViewLoanForm, UserPage

urlpatterns = [
	#Admin interface url
    url(r'^admin/', include(admin.site.urls)),
    #All urls for the authentication, signin, signup, login, logout, etc... From the allauth module
    url(r'^accounts/', include('allauth.urls')),
    #Buiness rest url and front end input form
    url(r'^business/', AddViewBusiness.as_view(), name='business'),
    url(r'^business_form/', AddViewBusinessForm),
    #Loan rest url and front end input form
    url(r'^loan_form/', AddViewLoanForm),
    url(r'^loan/', AddViewLoan.as_view(), name='loan'),
    #The user page will be shown at the end of the process of requesting a new loan, as a way to show that it was successful
    url(r'^user_page/', UserPage),
    #Home page url
    url(r'^$', HomePage)
]
