"""
Front end application tests file.
We want to test different aspects of the front end, but mainly that the pages present required html elements and that the
forms to input and show data are working.
"""
from django.test import TestCase
from django.core.urlresolvers import resolve
from frontend.views import HomePage, AddViewBusinessForm, AddViewLoanForm, UserPage
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

#To be recovered when fixing the signup tests from forms from allauth.socialaccount.views import signup

#Tests for the home page Unauthenticated user and main functions, only tested here to not be repeated in the Authenticated tests
class UrlTestsMainPage(TestCase):
    #We need to check that the home page url exist and it's being parsed correctly
    def test_frontend_url_resolves_to_main_page(self):
        found = resolve('/')
        self.assertEqual(found.func, HomePage)

    #We need to check that the templates for the home page exist and pass some basic tests
    def test_frontend_main_page_returns_correct_html_file(self):
        request = HttpRequest()
        response = HomePage(request)
        rendered_html = render_to_string('home_page.html')
        self.assertTrue(response.content.decode(), rendered_html)


    def test_frontend_main_page_returns_correct_html_parts(self):
        request = HttpRequest()
        response = HomePage(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<p><a href="accounts/login">Login</a></p>', response.content)
        self.assertIn(b'<p><a href="accounts/signup">SignUp</a></p>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

#Tests for the home page Authenticated
class UrlTestsMainPage(TestCase):

    #We need to create a user to be used by the authentication in all tests 
    def setUp(self):
        User.objects.create_user('temp_user', 'temporary@gmail.com', 'temp_user_password')

    def test_frontend_main_page_returns_correct_html_parts(self):
        self.client.login(username='temp_user', password='temp_user_password')
        response = self.client.get('/')
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'Welcome', response.content)
        self.assertIn(b'<a href="business_form/">Request loan</a>', response.content)
        self.assertIn(b'<a href="accounts/logout">Logout</a>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


#Tests for the Business form 
class UrlTestsBusinessForm(TestCase):

    #We need to create a user to be used by the authentication in all tests 
    def setUp(self):
        User.objects.create_user('temp_user', 'temporary@gmail.com', 'temp_user_password')

    #We need to check that the business form url exist and it's being parsed correctly
    def test_frontend_url_resolves_to_business_form(self):
        found = resolve('/business_form/')
        self.assertEqual(found.func, AddViewBusinessForm)

    #We need to check that the templates for the business form page exist and pass some basic tests
    def test_frontend_business_form_returns_correct_html_file(self):
        self.client.login(username='temp_user', password='temp_user_password')
        response = self.client.get('/business_form/')
        rendered_html = render_to_string('business_form.html')
        self.assertTrue(response.content.decode(), rendered_html)

    def test_frontend_business_form_returns_correct_html_parts_sample(self):
        self.client.login(username='temp_user', password='temp_user_password')
        response = self.client.get('/business_form/')
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<h1>Please add your business here, or select a previous one</h1>', response.content)
        self.assertIn(b'<form id=business_form action="/business/" method="POST">', response.content)
        self.assertIn(b'Registered company number:', response.content)
        self.assertIn(b'Business sector:', response.content)
        self.assertIn(b'<label for="id_address1"', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


#Tests for the Loan form 
class UrlTestsLoanForm(TestCase):

    #We need to create a user to be used by the authentication in all tests 
    def setUp(self):
        User.objects.create_user('temp_user', 'temporary@gmail.com', 'temp_user_password')

    #We need to check that the loan form url exist and it's being parsed correctly
    def test_frontend_url_resolves_to_loan_form(self):
        found = resolve('/loan_form/')
        self.assertEqual(found.func, AddViewLoanForm)

    #We need to check that the templates for the loan form page exist and pass some basic tests
    def test_frontend_loan_form_returns_correct_html_file(self):
        self.client.login(username='temp_user', password='temp_user_password')
        response = self.client.get('/loan_form/')
        rendered_html = render_to_string('loan_form.html')
        self.assertTrue(response.content.decode(), rendered_html)

    def test_frontend_loan_form_returns_correct_html_parts_sample(self):
        self.client.login(username='temp_user', password='temp_user_password')
        response = self.client.get('/loan_form/')
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<h1>Please fill in the data for the loand, and select the business you want to request the loan for</h1>', response.content)
        self.assertIn(b'<form id=loan_form action="/loan/" method="POST">', response.content)
        self.assertIn(b'Amount:', response.content)
        self.assertIn(b'Number of days:', response.content)
        self.assertIn(b'Business name:', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


#Tests for the User page form 
class UrlTestsUserPage(TestCase):
    #We need to create a user to be used by the authentication in all tests 
    def setUp(self):
        User.objects.create_user('temp_user', 'temporary@gmail.com', 'temp_user_password')

    #We need to check that the user page form url exist and it's being parsed correctly
    def test_frontend_url_resolves_to_user_page(self):
        found = resolve('/user_page/')
        self.assertEqual(found.func, UserPage)

    #We need to check that the templates for the user page exist and pass some basic tests
    def test_frontend_user_page_returns_correct_html_file(self):
        self.client.login(username='temp_user', password='temp_user_password')
        response = self.client.get('/user_page/')
        rendered_html = render_to_string('user_page.html')
        self.assertTrue(response.content.decode(), rendered_html)

    def test_frontend_user_page_returns_correct_html_parts(self):
        self.client.login(username='temp_user', password='temp_user_password')
        response = self.client.get('/user_page/')
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b"<h1>Thanks, your loan request has been received and it's being proccessed</h1>", response.content)
        self.assertIn(b'<h2>These are the details of your latest loan:</h2>', response.content)
        self.assertIn(b'<h2>These are all your other loans:</h2>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


