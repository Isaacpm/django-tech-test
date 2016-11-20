from django.conf.urls import include, url
from django.contrib import admin
#Import all views from the loans and frontend applications, as we are using all of them.
from loans.views import *
from frontend.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^business/', AddViewBusiness, name='business'),
    url(r'^business_form/', AddViewBusinessForm),
    url(r'^loan/', AddViewLoan.as_view(), name='loan'),
    url(r'^$', HomePage)
]
