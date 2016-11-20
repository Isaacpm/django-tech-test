from django.test import TestCase
from django.core.urlresolvers import resolve
from frontend.views import HomePage
from django.http import HttpRequest
from django.template.loader import render_to_string

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
