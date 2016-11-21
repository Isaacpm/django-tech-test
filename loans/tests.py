"""
Tests for the loans application, we want to tests the models and the rest api responses
"""
from django.test import TestCase
from django.contrib.auth.models import User
from loans.models import Business, Loan

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

