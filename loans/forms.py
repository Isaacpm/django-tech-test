"""
The custom signup form expands the default sign in form and adds phone number to the user profile used by all-auth
"""
from django import forms
from loans.models import Profile 

#Modified signup form to add phone number
class SignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number',)
    # A custom method required to work with django-allauth
    def signup(self, request, user):
        # Save your user
        user.save()
        # Save your profile
        profile = Profile()
        profile.user = user
        profile.phone_number = self.cleaned_data['phone_number']
        profile.save()