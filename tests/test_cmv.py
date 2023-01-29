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
