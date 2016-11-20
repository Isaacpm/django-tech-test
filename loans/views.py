from django.shortcuts import render, get_object_or_404
from loans.models import Business, Loan
from loans.serializers import BusinessSerializer, LoanSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

# Home page view, it loads the home page, from where all links are accessed
def HomePage(request):
    return render(request,'home_page.html')

def AddViewBusinessForm(request):
    return render(request,'business_form.html')

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
        return redirect('/')

def AddViewLoanForm(request):
    return render(request,'loan_form.html')

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