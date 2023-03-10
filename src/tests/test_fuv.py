from unittest import TestCase
from os import path
import yaml
from main.fuv import FUV

"""TestFUV"""


class TestFUV(TestCase):
    """TestFUV class

    Contains all the test cases for all FUV conditions.
    """

    def test_fuv_positive_condition_1(self):
        """Positive test for condition 1 of fuv method

        Check whether the elements of FUV are true if condition 1 is satisfied and condition 2 is not satisfied.
        (Condition 1: PUV[i] is false)
        (Condition 2: all elements in PUM row i are true)
        """

        puv = [False for _ in range(15)]
        pum = [[False for _ in range(15)] for _ in range(15)]
        fuv_answer = [True for _ in range(15)]
        self.assertEqual(FUV.fuv(puv, pum), fuv_answer)

    def test_fuv_positive_condition_2(self):
        """Positive test for condition 2 of fuv method

        Check whether the elements of FUV are true if condition 2 is satisfied and condition 1 is not satisfied.
        (Condition 1: PUV[i] is false)
        (Condition 2: all elements in PUM row i are true)
        """

        puv = [True for _ in range(15)]
        pum = [[True for _ in range(15)] for _ in range(15)]
        fuv_answer = [True for _ in range(15)]
        self.assertEqual(FUV.fuv(puv, pum), fuv_answer)

    def test_fuv_negative(self):
        """Negative test for fuv method

        Check whether the elements of FUV are false if both condition 1 and condition 2 are not satisfied.
        (Condition 1: PUV[i] is false)
        (Condition 2: all elements in PUM row i are true)
        """

        puv = [True for _ in range(15)]
        pum = [[None, False, True, True, True, True, True, True, True, True, True, True, True, True, True],
               [True, None, False, True, True, True, True, True, True, True, True, True, True, True, True],
               [True, True, None, False, True, True, True, True, True, True, True, True, True, True, True],
               [True, True, True, None, False, True, True, True, True, True, True, True, True, True, True],
               [True, True, True, True, None, False, True, True, True, True, True, True, True, True, True],
               [True, True, True, True, True, None, False, True, True, True, True, True, True, True, True],
               [True, True, True, True, True, True, None, False, True, True, True, True, True, True, True],
               [True, True, True, True, True, True, True, None, False, True, True, True, True, True, True],
               [True, True, True, True, True, True, True, True, None, False, True, True, True, True, True],
               [True, True, True, True, True, True, True, True, True, None, False, True, True, True, True],
               [True, True, True, True, True, True, True, True, True, True, None, False, True, True, True],
               [True, True, True, True, True, True, True, True, True, True, True, None, False, True, True],
               [True, True, True, True, True, True, True, True, True, True, True, True, None, False, True],
               [True, True, True, True, True, True, True, True, True, True, True, True, True, None, False],
               [False, True, True, True, True, True, True, True, True, True, True, True, True, True, None]]
        fuv_answer = [False for _ in range(15)]
        self.assertEqual(FUV.fuv(puv, pum), fuv_answer)

    def test_fuv_random_assignment(self):
        """Test for fuv method with a random assignment

        Check whether the elements of FUV are corresponding to the results when the variables are assigned randomly.
        (Condition 1: PUV[i] is false)
        (Condition 2: all elements in PUM row i are true)
        eg. puv[3] = True, which doesn't satisfy condition 1,
            all elements in PUM row 3 are true, which satisfies condition 2,
            Thus the result is fuv_answer[3] = True.
        """

        puv = [True, False, True, True, True, True, False, False, True, False, True, True, True, True, False]
        pum = [[None, False, True, True, True, True, True, True, True, True, True, True, True, True, True],
               [True, None, True, False, True, True, False, True, True, True, True, True, True, True, True],
               [True, True, None, False, False, True, True, False, True, True, True, True, True, True, True],
               [True, True, True, None, True, True, True, True, True, True, True, True, True, True, True],
               [True, True, True, True, None, False, False, True, True, True, True, True, True, True, True],
               [True, True, True, True, True, None, False, True, True, True, True, True, True, False, True],
               [False, True, True, True, True, True, None, True, True, True, False, True, True, True, True],
               [True, True, True, True, True, True, True, None, False, True, True, True, True, True, True],
               [True, True, True, True, True, True, True, True, None, True, True, True, True, True, True],
               [True, True, False, True, False, True, True, True, True, None, False, True, True, True, True],
               [True, True, True, True, True, True, True, True, True, True, None, False, True, True, True],
               [False, False, False, False, False, False, False, False, True, True, True, None, False, True, True],
               [True, True, True, True, True, True, True, True, True, True, True, True, None, True, False],
               [True, True, True, True, True, True, True, True, True, True, True, True, True, None, True],
               [True, True, True, True, True, True, True, True, True, True, True, True, True, True, None],
               ]
        fuv_answer = [False, True, False, True, False, False, True, True, True, True, False, False, False, True, True]
        self.assertEqual(FUV.fuv(puv, pum), fuv_answer)


    def test_fuv_invalid_input(self):
        """Invalid test for fuv method

        Check whether invalid input (puv) of fuv can be detected
        """

        pum = [[True for _ in range(15)] for _ in range(15)]

        file_path = path.abspath(path.join(path.dirname(__file__), "input/test_calc_fuv_invalid_input.yml"))
        with open(file_path, 'r') as f:
            input = yaml.safe_load(f)
        with self.assertRaises(ValueError):
            FUV(input, pum).calc_FUV()

    def test_fuv_invalid_pum(self):
        """Invalid test for fuv method

        Check whether invalid input (pum) of fuv can be detected
        """

        pum = [[True for _ in range(14)] for _ in range(16)]
        file_path = path.abspath(path.join(path.dirname(__file__), "input/input.yml"))
        with open(file_path, 'r') as f:
            input = yaml.safe_load(f)
        with self.assertRaises(ValueError):
            FUV(input, pum).calc_FUV()