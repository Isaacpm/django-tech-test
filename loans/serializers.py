from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
#We are going to use all the classes from the models file
from loans.models import Business, Loan

class BusinessSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Business
        fields = ('id', 'business_name', 'registered_company_number','business_sector','address1','address2','post_code','city_name','user')

class LoanSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Loan
        fields = ('id', 'amount', 'number_of_days', 'reason', 'business_name','user')