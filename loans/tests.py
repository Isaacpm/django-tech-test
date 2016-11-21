"""
Tests for the loans application, we want to tests the models and the rest api responses
"""
from django.test import TestCase
from django.contrib.auth.models import User
from loans.models import Business, Loan
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status

#Tests for the DB models
class ModelsTests(TestCase):
    def test_creating_user(self):
        user_object = User()
        user_object.name = "test"
        user_object.phone_number = "12345678"
        user_object.email = "test@testing.com"
        user_object.save()

    def test_creating_business(self):
        #We need a user object first in order to be able to add the business
        user_object = User()
        user_object.name = "test"
        user_object.phone_number = "12345678"
        user_object.email = "test@testing.com"
        user_object.save()

        business_object = Business()
        business_object.business_name = "Test business"
        business_object.registered_company_number = "12345678"
        business_object.business_sector = "Food & Drink"
        business_object.user = user_object
        business_object.address1 = "Test Address 1"
        business_object.address2 = "Test Address 2"
        business_object.post_code = "ES1 34GH"
        business_object.city_name = "London"
        business_object.save()

    def test_creating_loans(self):
        #We need a user object first in order to be able to add the business
        user_object = User()
        user_object.name = "test"
        user_object.phone_number = "12345678"
        user_object.email = "test@testing.com"
        user_object.save()

        #We need a business object in order to to be able to add the loan
        business_object = Business()
        business_object.business_name = "Test business"
        business_object.registered_company_number = "12345678"
        business_object.business_sector = "Food & Drink"
        business_object.user = user_object
        business_object.address1 = "Test Address 1"
        business_object.address2 = "Test Address 2"
        business_object.post_code = "ES1 34GH"
        business_object.city_name = "London"
        business_object.save()

        #We need a user object first in order to be able to add the business
        loan_object = Loan()
        loan_object.number_of_days = 25
        loan_object.amount = 50000
        loan_object.reason = "Test Loan"
        loan_object.user = user_object
        loan_object.business_name = business_object
        loan_object.save()

#Tests for REST API
class CreateLoanFlow(APITestCase):
    def setUp(self):
        User.objects.create_user('temp_user', 'temporary@gmail.com', 'temp_user_password')

    #Create loan flow, first create business, then a loan
    def test_create_loan_flow(self):
        """
        Ensure we can create a new Business object.
        """
        self.client.login(username='temp_user', password='temp_user_password')
        url = reverse('business')
        #Defining the business name here to make sure we use the same text in the two places we need it, in the data and in the assertEqual test. 
        business_name = 'Test business'
        data = {'business_name': business_name,'registered_company_number': '12345678','business_sector': 'RE','address1': 'Address test line 1','address2': 'Address test line 2','post_code': 'XXX XXX','city_name': 'London'}
        response = self.client.post(url, data, format='json')
        #We are going to make sure that we get an http 201 for a created object, that the Business table has one object and that the name of the object is the same as the one used for the test
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Business.objects.count(), 1)
        self.assertEqual(Business.objects.get().business_name, business_name)
        #We need the id of the insterted object in order to use it to create the loan
        business_id = response.data.get("id")
        """
        After creating the business we use it to create a loan
        """
        url = reverse('loan')
        #Defining the loan's reason here to make sure we use the same in the two places we need it, in the data and in the assertEqual test. 
        loan_reason = 'We are testing the loan creation, we do not really need any money'
        data = {'business_name': 'Test business','amount': '20000','number_of_days': '12','reason': loan_reason,'business_name': business_id}
        response = self.client.post(url, data, format='json')
        #We are going to make sure that we get an http 201 for a created object, that the Loan table has one object and that the reason of the object is the same as the one used for the test
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Loan.objects.count(), 1)
        self.assertEqual(Loan.objects.get().reason, loan_reason)



