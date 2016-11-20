from django.test import TestCase
from django.core.urlresolvers import resolve
from loans.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

#We need to check that the frontend urls exist and being parsed correctly
class UrlTests(TestCase):

    def test_frontend_url_resolves_to_main_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

#We need to check that the templates exist and pass some basic tests
    def test_frontend_main_page_returns_correct_html_file(self):
        request = HttpRequest()
        response = home_page(request)
        rendered_html = render_to_string('home_page.html')
        self.assertTrue(response.content.decode(), rendered_html)


    def test_frontend_main_page_returns_correct_html_parts(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<p><a href="accounts/login">Login</a></p>', response.content)
        self.assertIn(b'<p><a href="business/">Request loan</a></p>', response.content)
        self.assertIn(b'<p><a href="accounts/signup">SignUp</a></p>', response.content)
        self.assertIn(b'<p><a href="accounts/logout">Logout</a></p>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
