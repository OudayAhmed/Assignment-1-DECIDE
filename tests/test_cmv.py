import unittest
from unittest import TestCase
from src.cmv import CMV


class TestCMV(TestCase):

    def test_cmv_9_positive(self):
        """Positive test for cmv 9 method"""

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.5, 0.8], [0.3, 0.2], [0.2, 0.3], [0.3, 0.9]]
        c_pts = 1
        d_pts = 2
        epsilon = 0.5
        self.assertTrue(CMV.cmv9(numpoints, points, c_pts, d_pts, epsilon))

    def test_cmv_9_negative(self):
        """Negative test for cmv 9 method"""

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        c_pts = 2
        d_pts = 2
        epsilon = 0.3
        self.assertFalse(CMV.cmv9(numpoints, points, c_pts, d_pts, epsilon))

    def test_cmv_9_negative_epsilon(self):
        """Test case for cmv 9 method with negative EPSILON"""

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        c_pts = 2
        d_pts = 2
        epsilon = -0.8
        self.assertFalse(CMV.cmv9(numpoints, points, c_pts, d_pts, epsilon))

    def test_cmv_9_negative_c_pts(self):
        """Test case for cmv 9 method with negative C_PTS"""

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        c_pts = -1
        d_pts = 2
        epsilon = 0.3
        self.assertFalse(CMV.cmv9(numpoints, points, c_pts, d_pts, epsilon))