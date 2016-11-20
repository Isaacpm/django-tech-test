from django import forms
from loans.models import Business 

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'
        exclude = ["user"]