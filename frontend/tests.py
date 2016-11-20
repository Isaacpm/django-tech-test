from django.test import TestCase
from django.core.urlresolvers import resolve
from frontend.views import HomePage, AddViewBusinessForm
from django.http import HttpRequest
from django.template.loader import render_to_string

#To be recovered when fixing the signup tests from forms from allauth.socialaccount.views import signup

#We need to check that the home page url exist and it's being parsed correctly
class UrlTests(TestCase):

    def test_frontend_url_resolves_to_main_page(self):
        found = resolve('/')
        self.assertEqual(found.func, HomePage)

#We need to check that the templates for the home page exist and pass some basic tests
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

#We need to check that the home page url exist and it's being parsed correctly
class UrlTests(TestCase):

    def test_frontend_url_resolves_to_main_page(self):
        found = resolve('/business_form/')
        self.assertEqual(found.func, AddViewBusinessForm)

#We need to check that the templates for the home page exist and pass some basic tests
    def test_frontend_main_page_returns_correct_html_file(self):
        request = HttpRequest()
        response = AddViewBusinessForm(request)
        rendered_html = render_to_string('business_form.html')
        self.assertTrue(response.content.decode(), rendered_html)

    def test_frontend_main_page_returns_correct_html_parts_unauthenticated_user(self):
        request = HttpRequest()
        response = AddViewBusinessForm(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<h1>Please add your business here, or select a previous one</h1>', response.content)
        self.assertIn(b'<form action="/business/" method="POST">', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))