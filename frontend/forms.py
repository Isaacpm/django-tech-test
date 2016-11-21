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