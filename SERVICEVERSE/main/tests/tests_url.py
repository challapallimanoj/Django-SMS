from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import *


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('main')
        print(resolve(url))
