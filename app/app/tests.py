"""
Simple Test
"""

from django.test import SimpleTestCase

from app import Calc


class calctests(SimpleTestCase):
    """Test: the calc modules. """
    def test_add_numbers(self):
        res = Calc.add(5, 8)
        self.assertEqual(res, 13)

    def test_subtract_number(self):
        "Test subtracting number"
        res = Calc.subtract(10, 15)
        self.assertEqual(res, 5)
