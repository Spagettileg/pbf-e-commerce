from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Product models.
    """
    
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
    

