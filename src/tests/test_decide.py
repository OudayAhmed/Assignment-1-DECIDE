from unittest import TestCase
from os import path
import yaml

from main.decide import Decide


class TestCMV(TestCase):

    def test_decide_positive(self):
        """Positive test for decide method"""

        file_path = path.abspath(path.join(path.dirname(__file__), "input/test_decide_positive.yml"))
        with open(file_path, 'r') as f:
            input = yaml.safe_load(f)
        self.assertTrue(Decide(input).decide())

    def test_decide_negative(self):
        """Negative test for decide method"""

        file_path = path.abspath(path.join(path.dirname(__file__), "input/test_decide_negative.yml"))
        with open(file_path, 'r') as f:
            input = yaml.safe_load(f)
        self.assertFalse(Decide(input).decide())

    def test_decide_numpoints_equal_one(self):
        """Test case for decide method with only one point."""

        file_path = path.abspath(path.join(path.dirname(__file__), "input/test_decide_numpoints_equal_one.yml"))
        with open(file_path, 'r') as f:
            input = yaml.safe_load(f)
        with self.assertRaises(ValueError):
            Decide(input).decide()
