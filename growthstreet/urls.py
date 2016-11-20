from django.conf.urls import include, url
from django.contrib import admin
#Import all views from the loans applications, as we will use all of them.
from loans.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^business/', include('allauth.urls')),
    url(r'^loan/', include('allauth.urls')),
    url(r'^$', HomePage)
]
