from django.urls import reverse, resolve
from django.test import TestCase
from ..views import home

class HomeTests(TestCase):

    def test_status_code(self):
        url = reverse('accounts:home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolves(self):
        view = resolve('/accounts/')
        self.assertEquals(view.func, home)
