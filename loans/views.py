from django.shortcuts import render
from loans.models import Business, Loan
from loans.serializers import BusinessSerializer, LoansSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

# Home page view, it loads the home page, from where all links are accessed
def HomePage(request):
    return render(request,'home_page.html')

class AddViewBusiness(viewsets.ModelViewSet):
    """
    API endpoint that allows business to be viewed or edited.
    """
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class AddViewLoan(viewsets.ModelViewSet):
    """
    API endpoint that allows business to be viewed or edited.
    """
    queryset = Loan.objects.all()
    serializer_class = LoansSerializer