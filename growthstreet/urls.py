from django.conf.urls import include, url
from django.contrib import admin
#Import all views from the loans applications, as we will use all of them.
from loans.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_page)
]
