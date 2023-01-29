import unittest
from unittest import TestCase
from src.cmv import CMV


class TestCMV(TestCase):
    def test_cmv_2_positive(self):
        """Positive test for cmv2 method"""
        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        epsilon = 0.5
        self.assertTrue(CMV.cmv2(points, epsilon))

    def test_cmv_2_negative(self):
        """Negative test for cmv2 method"""
        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        epsilon = 3
        self.assertFalse(CMV.cmv2(points, epsilon))

    def test_cmv_2_negative_epsilon(self):
        """Test case for cmv2 method with negative EPSILON"""
        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        epsilon = -0.3
        self.assertFalse(CMV.cmv2(points, epsilon))
