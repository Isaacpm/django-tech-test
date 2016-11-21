from loans.models import Business, Loan
from loans.serializers import BusinessSerializer, LoanSerializer
from rest_framework import generics
from django.contrib.auth.decorators import login_required

class AddViewBusiness(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class AddViewLoan(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
