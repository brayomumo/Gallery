from django.test import TestCase

# Create your tests here.

from .models import Location,categories,Image
import datetime as dt
# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.kitui= Location(location='Nyeri')

    def test_instance(self):
        self.assertTrue(isinstance(self.kitui,Location))