from django.test import TestCase
from django.core.urlresolvers import resolve
from loans.views import HomePage
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from loans.models import Business, Loan
#To be recovered when fixing the signup tests from forms from allauth.socialaccount.views import signup

#We need to check that the frontend urls exist and being parsed correctly
class UrlTests(TestCase):

    def test_frontend_url_resolves_to_main_page(self):
        found = resolve('/')
        self.assertEqual(found.func, HomePage)

#We need to check that the templates exist and pass some basic tests
    def test_frontend_main_page_returns_correct_html_file(self):
        request = HttpRequest()
        response = HomePage(request)
        rendered_html = render_to_string('home_page.html')
        self.assertTrue(response.content.decode(), rendered_html)


    def test_frontend_main_page_returns_correct_html_parts_unauthenticated_user(self):
        request = HttpRequest()
        response = HomePage(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<p><a href="accounts/login">Login</a></p>', response.content)
        self.assertIn(b'<p><a href="accounts/signup">SignUp</a></p>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


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
        loan_object.business = business_object
        loan_object.save()

"""
#Tests for the User Signup function
We need to fix this to use the signup forms through http request
class UserSignupTests(TestCase):
    def test_signingup_user_POST_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST['name'] = "Test"
        request.POST['phone_number'] = "12345678"
        request.POST['email'] = "test@testing.com"
        response = signup(request)

        check to see if the user was added to fix later, as it's not using the same DB for the test as for the insertion, the test db is temp
        new_user = User.objects.first()
        self.assertEqual(new_user.name, 'Test')

    def test_signingup_user_POST_request_redirection(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST['name'] = "Test"
        request.POST['phone_number'] = "12345678"
        request.POST['email'] = "test@testing.com"
        response = signup(request)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')
"""

