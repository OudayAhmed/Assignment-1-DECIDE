from unittest import TestCase
import yaml
from os import path

from main.pum import PUM

class TestCMV(TestCase):

    def test_calc_pum_positive(self):
        """Positive test for calc_PUM method

        Check whether the elements obtained by calc_PUM() are as expected,
        which should be all true.
        """

        cmv = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        file_path = path.abspath(path.join(path.dirname(__file__), "input/test_calc_pum_positive.yml"))
        with open(file_path, 'r') as f:
            input = yaml.safe_load(f)
        pum_expected = [
            [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1]]
        self.assertEqual(PUM(input, cmv).calc_PUM(), pum_expected)

    def test_calc_pum_negative(self):
        """Negative test for calc_PUM method

        Check whether the elements obtained by calc_PUM() are as expected,
        which should be all true except for pum[3][13] and pum[13][3].
        """

        cmv = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        file_path = path.abspath(path.join(path.dirname(__file__), "input/test_calc_pum_negative.yml"))
        with open(file_path, 'r') as f:
            input = yaml.safe_load(f)
        pum_expected = [
            [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1]]
        self.assertNotEqual(PUM(input, cmv).calc_PUM(), pum_expected)

    def test_calc_pum_lcm_asymmetric(self):
        """Invalid test for pum method

        Check whether invalid (asymmetric) input (lcm) of fuv can be detected
        """

        cmv = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        file_path = path.abspath(path.join(path.dirname(__file__), "input/test_calc_pum_lcm_asymmetric.yml"))
        with open(file_path, 'r') as f:
            input = yaml.safe_load(f)
        with self.assertRaises(ValueError):
            PUM(input, cmv).calc_PUM()

    def test_calc_pum_invalid_cmv(self):
        """Invalid test for pum method

        Check whether invalid input (cmv) of pum can be detected
        """

        cmv = [True for _ in range(14)]
        file_path = path.abspath(path.join(path.dirname(__file__), "input/input.yml"))
        with open(file_path, 'r') as f:
            input = yaml.safe_load(f)
        with self.assertRaises(ValueError):
            PUM(input, cmv).calc_PUM()