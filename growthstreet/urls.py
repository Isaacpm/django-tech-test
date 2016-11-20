from django.conf.urls import include, url
from django.contrib import admin
#Import required views from loans and frontend applications
from loans.views import AddViewBusiness, AddViewLoan
from frontend.views import HomePage, AddViewBusinessForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^business/', AddViewBusiness, name='business'),
    url(r'^business_form/', AddViewBusinessForm),
    url(r'^loan/', AddViewLoan.as_view(), name='loan'),
    url(r'^$', HomePage)
]
