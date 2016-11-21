"""
Loans applications views file, it creates the views to be used by the application in order to access
the data.
"""
from loans.models import Business, Loan
from loans.serializers import BusinessSerializer, LoanSerializer
from rest_framework import generics
from django.contrib.auth.decorators import login_required

#Default serializer view for business, it allows us to create and list the business for each user
class AddViewBusiness(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

#Default serializer view for loan, it allows us to create and list the loans for each user
class AddViewLoan(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
