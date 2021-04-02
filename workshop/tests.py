from django.test import TestCase
from django.urls import reverse
from .views import AccueilView

class AccueilPageTestCase(TestCase):
    """
    Test that accueil page returns a 200 if the item exists.
    """
    def test_accueil_page(self):
        response = self.client.get(reverse('workshop:accueil'))
        self.assertEqual(response.status_code, 200)


class WorkPageTestCase(TestCase):
    """
    Test that about page returns a 200 if the item exists.
    """
    def test_accueil_page(self):
        response = self.client.get(reverse('workshop:work'))
        self.assertEqual(response.status_code, 200)


class Work01PageTestCase(TestCase):
    """
    Test that wor01 page returns a 200 if the item exists.
    """
    def test_accueil_page(self):
        response = self.client.get(reverse('workshop:work01'))
        self.assertEqual(response.status_code, 200)


class Work02PageTestCase(TestCase):
    """
    Test that work02 page returns a 200 if the item exists.
    """
    def test_accueil_page(self):
        response = self.client.get(reverse('workshop:work02'))
        self.assertEqual(response.status_code, 200)


class Work03PageTestCase(TestCase):
    """
    Test that work03 page returns a 200 if the item exists.
    """
    def test_accueil_page(self):
        response = self.client.get(reverse('workshop:work03'))
        self.assertEqual(response.status_code, 200)