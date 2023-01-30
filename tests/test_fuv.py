from unittest import TestCase
from src.fuv import FUV

"""TestFUV"""


class TestFUV(TestCase):
    """TestFUV class

    Contains all the test cases for all FUV conditions.
    """

    def test_fuv_positive_condition_1(self):
        """Positive test for condition 1 of fuv method"""

        puv = [False for _ in range(14)]
        pum = [[False for _ in range(14)] for _ in range(14)]
        answer = [True for _ in range(14)]
        self.assertEqual(FUV.fuv(puv, pum), answer)

    def test_fuv_positive_condition_2(self):
        """Positive test for condition 2 of fuv method"""

        puv = [True for _ in range(14)]
        pum = [[True for _ in range(14)] for _ in range(14)]
        answer = [True for _ in range(14)]
        self.assertEqual(FUV.fuv(puv, pum), answer)

    def test_fuv_negative(self):
        """Negative test for fuv method"""

        puv = [True for _ in range(14)]
        pum = [[None, False, True, True, True, True, True, True, True, True, True, True, True, True],
               [True, None, False, True, True, True, True, True, True, True, True, True, True, True],
               [True, True, None, False, True, True, True, True, True, True, True, True, True, True],
               [True, True, True, None, False, True, True, True, True, True, True, True, True, True],
               [True, True, True, True, None, False, True, True, True, True, True, True, True, True],
               [True, True, True, True, True, None, False, True, True, True, True, True, True, True],
               [True, True, True, True, True, True, None, False, True, True, True, True, True, True],
               [True, True, True, True, True, True, True, None, False, True, True, True, True, True],
               [True, True, True, True, True, True, True, True, None, False, True, True, True, True],
               [True, True, True, True, True, True, True, True, True, None, False, True, True, True],
               [True, True, True, True, True, True, True, True, True, True, None, False, True, True],
               [True, True, True, True, True, True, True, True, True, True, True, None, False, True],
               [True, True, True, True, True, True, True, True, True, True, True, True, None, False],
               [False, True, True, True, True, True, True, True, True, True, True, True, True, None]]
        answer = [False for _ in range(14)]
        self.assertEqual(FUV.fuv(puv, pum), answer)

    def test_fuv_random(self):
        """Test for fuv method with a random assignment"""

        puv = [True, False, True, True, True, True, False, False, True, False, True, True, True, True]
        pum = [[None, False, True, True, True, True, True, True, True, True, True, True, True, True],
               [True, None, True, False, True, True, False, True, True, True, True, True, True, True],
               [True, True, None, False, False, True, True, False, True, True, True, True, True, True],
               [True, True, True, None, True, True, True, True, True, True, True, True, True, True],
               [True, True, True, True, None, False, False, True, True, True, True, True, True, True],
               [True, True, True, True, True, None, False, True, True, True, True, True, True, False],
               [False, True, True, True, True, True, None, True, True, True, False, True, True, True],
               [True, True, True, True, True, True, True, None, False, True, True, True, True, True],
               [True, True, True, True, True, True, True, True, None, True, True, True, True, True],
               [True, True, False, True, False, True, True, True, True, None, False, True, True, True],
               [True, True, True, True, True, True, True, True, True, True, None, False, True, True],
               [False, False, False, False, False, False, False, False, True, True, True, None, False, True],
               [True, True, True, True, True, True, True, True, True, True, True, True, None, False],
               [True, True, True, True, True, True, True, True, True, True, True, True, True, None]]
        answer = [False, True, False, True, False, False, True, True, True, True, False, False, False, True]
        self.assertEqual(FUV.fuv(puv, pum), answer)
