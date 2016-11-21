"""
Forms file for the front end application.
The forms use the model form the django helper class.
We remove the user from the form, as this should be automatically selected from the logged in user
All other fields should appear and be used by the forms
"""

from django import forms
from loans.models import Business, Loan

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'
        exclude = ["user"]

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'
        exclude = ["user"]