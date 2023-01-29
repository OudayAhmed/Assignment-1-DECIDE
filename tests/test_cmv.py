import unittest
from unittest import TestCase
from src.cmv import CMV


class TestCMV(TestCase):
    def test_cmv5_negative(self):
        """Test case for CMV5 to check if the output is false when it should be false.

        Inputs are length of array containing datapoints and datapoints.
        Xi < Xj when it should be Xj < Xi.
        """

        points = [[0.2, 0.3], [0.4, 0.2], [0.3, 0.1]]
        numpoints = 3
        self.assertFalse(CMV.cmv5(numpoints, points))
    
    def test_cmv5_positive(self):
        """Test case for CMV5 to check if the output is true when it should be true.

        Inputs are length of array containing datapoints and datapoints.
        Xj < Xi.
        """
        
        points = [[0.4, 0.3], [0.2, 0.2], [0.1, 0.3]]
        numpoints = 3
        self.assertTrue(CMV.cmv5(numpoints, points))

    def test_cmv5_invalid(self):
        """Test case for CMV5 to check if the output is false when it should be false.

        Inputs are length of array containing datapoints and datapoints.
        Input is invalid to to check if input is properly validated.
        """
        
        points = [[0.4, 0.3]]
        numpoints = 1
        self.assertFalse(CMV.cmv5(numpoints,points))
