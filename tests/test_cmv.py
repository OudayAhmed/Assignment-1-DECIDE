import unittest
from unittest import TestCase
from src.cmv import CMV


class TestCMV(TestCase):

    def test_cmv0_negative(self):
        """Test case for CMV0 method with false sets of data points."""
        points = [[0.2, 0.3], [0.3, 0.4], [0.1, 0.3]]
        length1 = 0.3
        self.assertFalse(CMV.cmv0(points, length1))

    def test_cmv0_positive(self):
        """Test case for CMV0 method with at least one set of positive data points."""
        points = [[0.2, 0.3], [0.3, 0.4], [0.1, 0.3]]
        length1 = 0.1
        self.assertTrue(CMV.cmv0(points, length1))

    def test_cmv0_invalid(self):
        """Test case for CMV0 method with invalid input."""
        points = [[0.2, 0.3], [0.3, 0.4], [0.1, 0.3]]
        length1 = -0.1
        self.assertFalse(CMV.cmv0(points, length1))
        
    def test_cmv_2_positive(self):
        """Positive test for cmv 2 method"""
        
        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        epsilon = 0.5
        self.assertTrue(CMV.cmv2(points, epsilon))

    def test_cmv_2_negative(self):
        """Negative test for cmv 2 method"""
        
        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        epsilon = 3
        self.assertFalse(CMV.cmv2(points, epsilon))

    def test_cmv_2_negative_epsilon(self):
        """Test case for cmv 2 method with negative EPSILON"""
        
        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        epsilon = -0.3
        self.assertFalse(CMV.cmv2(points, epsilon))

    def test_cmv5_negative(self):
        """Test case for CMV5 method with false sets of data points."""

        points = [[0.2, 0.3], [0.4, 0.2], [0.3, 0.1]]
        numpoints = 3
        self.assertFalse(CMV.cmv5(numpoints, points))
    
    def test_cmv5_positive(self):
        """Test case for CMV5 method with at least one set of positive data points."""
        
        points = [[0.4, 0.3], [0.2, 0.2], [0.1, 0.3]]
        numpoints = 3
        self.assertTrue(CMV.cmv5(numpoints, points))

    def test_cmv5_invalid(self):
        """Test case for CMV5 method with invalid data points."""
        
        points = [[0.4, 0.3]]
        numpoints = 1
        self.assertFalse(CMV.cmv5(numpoints,points))

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
        
    def test_cmv_12_positive(self):
        """Positive test case for cmv 12"""
        
        numpoints = 3
        points = [[0.5, 0.4], [1.0, 0.7], [2.2, 0.7]]
        k_pts = 1
        length1 = 1
        length2 = 1
        self.assertTrue(CMV.cmv12(numpoints, points, k_pts, length1, length2))
        
    def test_cmv_12_negative(self):
        """Negative test case for cmv 12"""
        
        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        k_pts = 1
        length1 = 1
        length2 = 1
        self.assertFalse(CMV.cmv12(numpoints, points, k_pts, length1, length2))
        
    def test_cmv_12_negative(self):
        """Test case for cmv 12 method with less than 3 NUMPOINTS"""
        
        numpoints = 2
        points = [[0.1, 0.2], [0.8, 0.9]]
        k_pts = 1
        length1 = 1
        length2 = 1
        self.assertFalse(CMV.cmv12(numpoints, points, k_pts, length1, length2))
        
    def test_cmv_12_negative_length2(self):
        """Test case for cmv 12 method with negative LENGTH2"""
        
        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        k_pts = 2
        length1 = 1
        length2 = -1
        self.assertFalse(CMV.cmv12(numpoints, points, k_pts, length1, length2))
    
    def test_cmv_12_negative_k_pts(self):
        """Test case for cmv 12 method with negative K_PTS"""
        
        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        k_pts = -1
        length1 = 1
        length2 = 1
        self.assertFalse(CMV.cmv12(numpoints, points, k_pts, length1, length2))
    
        