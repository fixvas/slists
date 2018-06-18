from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):

    def test_home_page_resolves_to_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
