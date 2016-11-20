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
"""
class AddViewBusiness(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_view_business.html'

    def get(self, request):
        return render(request,'business.html')

    def post(self, request):
        business_objects = get_object_or_404(Business)
        serializer = BusinessSerializer(business_objects, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'business_objects': business_objects})
        serializer.save()
        return redirect('/loan/')
"""
class AddViewLoan(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_view_loan.html'

    def get(self, request):
        loan_objects = get_object_or_404(Loan)
        serializer = LoanSerializer(Loan)
        return Response({'serializer': serializer, 'loan_objects': loan_objects})

    def post(self, request,):
        business = get_object_or_404(Loan)
        serializer = LoanSerializer(Loan, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'loan_objects': loan_objects})
        serializer.save()
        return redirect('/')
