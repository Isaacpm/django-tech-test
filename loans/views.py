from django.shortcuts import render
from loans.models import Business, Loan
from loans.serializers import BusinessSerializer, LoanSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

# Home page view, it loads the home page, from where all links are accessed
def HomePage(request):
    return render(request,'home_page.html')

class AddViewBusiness(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_view_business.html'

    def get(self, request, pk):
        business_objects = get_object_or_404(Business)
        serializer = BusinessSerializer(business_objects)
        return Response({'serializer': serializer, 'business_objects': business_objects})

    def post(self, request, pk):
        business_objects = get_object_or_404(Business)
        serializer = BusinessSerializer(business_objects, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'business_objects': business_objects})
        serializer.save()
        return redirect('/')

class AddViewLoan(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_view_loan.html'

    def get(self, request, pk):
        loan_objects = get_object_or_404(Loan)
        serializer = LoanSerializer(Loan)
        return Response({'serializer': serializer, 'loan_objects': loan_objects})

    def post(self, request, pk):
        business = get_object_or_404(Loan)
        serializer = LoanSerializer(Loan, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'loan_objects': loan_objects})
        serializer.save()
        return redirect('/')