"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers togather"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)