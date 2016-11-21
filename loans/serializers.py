"""
Serializer definition file, we will use the serializers in this page to interact with the application models through the REST Framework
"""

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
#We are only going to need the Business and Loan classes from the loans models
from loans.models import Business, Loan

class BusinessSerializer(serializers.ModelSerializer):
    #The user is assigned from the signed on user
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Business
        fields = ('id', 'business_name', 'registered_company_number','business_sector','address1','address2','post_code','city_name','user')

class LoanSerializer(serializers.ModelSerializer):
    #The user is assigned from the signed on user
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Loan
        fields = ('id', 'amount', 'number_of_days', 'reason', 'business_name','user')