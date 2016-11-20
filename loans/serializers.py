from rest_framework import serializers
#We are going to use all the classes from the models file
from loans.models import Business, Loan

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'name', 'address_id', 'registered_company_number','business_sector','address1','address2','post_code','city_name')

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('id', 'amount', 'number_of_days', 'reason', 'business')