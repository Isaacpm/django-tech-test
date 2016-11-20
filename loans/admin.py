from django.contrib import admin

# Register your models here.
from django.contrib import admin
from loans.models import Loan, Business, Profile

# Register your models here.
admin.site.register(Business)
admin.site.register(Loan)
admin.site.register(Profile)