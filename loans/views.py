from django.shortcuts import render, get_object_or_404
from loans.models import Business, Loan
from loans.serializers import BusinessSerializer, LoanSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class AddViewBusiness(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class AddViewLoan(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = LoanSerializer
