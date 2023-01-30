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

    def test_cmv_1_positive(self):
        """Positive test for cmv 1 method"""

        numPoints = 4
        points = [[1, 3], [1, 1], [3, 1], [5, 2]]
        radius1 = 1.4
        self.assertTrue(CMV.cmv1(numPoints, points, radius1))

    def test_cmv_1_negative(self):
        """Negative test for cmv 1 method"""

        numPoints = 4
        points = [[1, 3], [1, 1], [3, 1], [5, 2]]
        radius1 = 2
        self.assertFalse(CMV.cmv1(numPoints, points, radius1))

    def test_cmv_1_negative_radius1(self):
        """Test case for cmv 1 method with negative RADIUS1"""

        numPoints = 4
        points = [[1, 3], [1, 1], [3, 1], [5, 2]]
        radius1 = -1.4
        self.assertFalse(CMV.cmv1(numPoints, points, radius1))

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

    def test_cmv_2_two_points_coincide(self):
        """Test case for cmv 2 method with two points coincide"""

        points = [[0.1, 0.2], [0.1, 0.2], [0.2, 0.3]]
        epsilon = 0.5
        self.assertFalse(CMV.cmv2(points, epsilon))

    def test_cmv_3_positive(self):
        """Positive test case for CMV3 method"""
        
        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        numpoints = 3
        area1 = 0.01
        self.assertTrue(CMV.cmv3(numpoints, points, area1))

    def test_cmv_3_negative(self):
        """negative test case for CMV3 method, AREA1 > TRIANGLEAREA"""

        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        numpoints = 3
        area1 = 1
        self.assertFalse(CMV.cmv3(numpoints, points, area1))

    def test_cmv_3_negative_area(self):
        """Test case for CMV3 method with negative AREA1"""

        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        numpoints = 3
        area1 = -1
        self.assertFalse(CMV.cmv3(numpoints, points, area1))

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
    
    def test_cmv7_positive(self):
        """Positive test for CMV 7 method"""

        numpoints = 3
        points = [[0.1, 0.3], [0.2, 0.1], [0.3, 0.4]]
        k_pts = 1
        length1 = 0.1
        self.assertTrue(CMV.cmv7(numpoints, points, k_pts, length1))
    
    def test_cmv7_negative(self):
        """"Negative test for CMV 7 method"""

        numpoints = 4
        points = [[0.3, 0.2], [0.4, 0.1], [0.2, 0.5], [0.5, 0.3]]
        k_pts = 2
        length1 = 0.4
        self.assertFalse(CMV.cmv7(numpoints, points, k_pts, length1))

    def test_cmv7_negative_k_pts(self):
        """Test case for CMV7 with invalid k_pts"""

        numpoints = 3
        points = [[0.1, 0.3], [0.2, 0.1], [0.3, 0.4]]
        k_pts = -1
        length1 = 0.1
        self.assertFalse(CMV.cmv7(numpoints, points, k_pts, length1))

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

    def test_cmv_10_positive(self):
        """Positive test for cmv 10 method"""

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.5, 0.8], [0.3, 0.4], [0.2, 0.1], [0.5, 0.1]]
        e_pts = 1
        f_pts = 2
        area1 = 0.003
        self.assertTrue(CMV.cmv10(numpoints, points, e_pts, f_pts, area1))

    def test_cmv_10_negative(self):
        """Negative test for cmv 10 method"""

        numpoints = 5
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.5, 0.8], [0.2, 0.1]]
        e_pts = 1
        f_pts = 1
        area1 = 0.009
        self.assertFalse(CMV.cmv10(numpoints, points, e_pts, f_pts, area1))

    def test_cmv_10_only_three_numpoints(self):
        """Test case for cmv 10 method with only three NUMPOINTS"""

        numpoints = 3
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1]]
        e_pts = 1
        f_pts = 1
        area1 = 0.003
        self.assertFalse(CMV.cmv10(numpoints, points, e_pts, f_pts, area1))

    def test_cmv_10_negative_e_pts(self):
        """Test case for cmv 10 method with negative E_PTS"""

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.5, 0.8], [0.3, 0.4], [0.2, 0.1], [0.5, 0.1]]
        e_pts = -1
        f_pts = 1
        area1 = 0.002
        self.assertFalse(CMV.cmv10(numpoints, points, e_pts, f_pts, area1))

    def test_cmv_10_e_pts_and_f_pts_greater_than_numpoints_minus_three(self):
        """Test case for cmv 10 method with E_PTS + F_PTS > NUMPOINTS - 3"""

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.5, 0.8], [0.3, 0.4], [0.2, 0.1], [0.5, 0.1]]
        e_pts = 3
        f_pts = 4
        area1 = 0.001
        self.assertFalse(CMV.cmv10(numpoints, points, e_pts, f_pts, area1))

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

    def test_cmv_13_positive(self):
        """Positive test for cmv 13 method"""

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        A_PTS = 1
        B_PTS = 1
        radius1 = 0.3
        radius2 = 2.5
        self.assertTrue(CMV.cmv13(numPoints, points, A_PTS, B_PTS, radius1, radius2))

    def test_cmv_13_negative_fail_condition_1(self):
        """Negative test of condition 1 for cmv 13 method"""

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        A_PTS = 1
        B_PTS = 1
        radius1 = 2.5
        radius2 = 2.5
        self.assertFalse(CMV.cmv13(numPoints, points, A_PTS, B_PTS, radius1, radius2))

    def test_cmv_13_negative_fail_condition_2(self):
        """Negative test of condition 2 for cmv 13 method"""

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        A_PTS = 1
        B_PTS = 1
        radius1 = 0.3
        radius2 = 0.3
        self.assertFalse(CMV.cmv13(numPoints, points, A_PTS, B_PTS, radius1, radius2))

    def test_cmv_13_negative_radius2(self):
        """Test case for cmv 13 method with negative RADIUS2"""

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        A_PTS = 1
        B_PTS = 1
        radius1 = 0.3
        radius2 = -2.5
        self.assertFalse(CMV.cmv13(numPoints, points, A_PTS, B_PTS, radius1, radius2))

    def test_cmv_13_negative_NUMPOINTS(self):
        """Test case for cmv 13 method with negative NUMPOINTS"""

        numPoints = -3
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        A_PTS = 1
        B_PTS = 1
        radius1 = 0.3
        radius2 = 2.5
        self.assertFalse(CMV.cmv13(numPoints, points, A_PTS, B_PTS, radius1, radius2))

    def test_cmv_14_positive(self):
        """Positive test for cmv 14 method"""

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        E_PTS = 1
        F_PTS = 1
        area1 = 0.5
        area2 = 2.5
        self.assertTrue(CMV.cmv14(numPoints, points, E_PTS, F_PTS, area1, area2))

    def test_cmv_14_negative_fail_condition_1(self):
        """Negative test of condition 1 for cmv 14 method"""

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        E_PTS = 1
        F_PTS = 1
        area1 = 2.5
        area2 = 2.5
        self.assertFalse(CMV.cmv14(numPoints, points, E_PTS, F_PTS, area1, area2))

    def test_cmv_14_negative_fail_condition_2(self):
        """Negative test of condition 2 for cmv 14 method"""

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        E_PTS = 1
        F_PTS = 1
        area1 = 0.5
        area2 = 0.5
        self.assertFalse(CMV.cmv14(numPoints, points, E_PTS, F_PTS, area1, area2))

    def test_cmv_14_negative_area2(self):
        """Test case for cmv 14 method with negative AREA2"""

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        E_PTS = 1
        F_PTS = 1
        area1 = 0.5
        area2 = -2.5
        self.assertFalse(CMV.cmv14(numPoints, points, E_PTS, F_PTS, area1, area2))

    def test_cmv_14_negative_NUMPOINTS(self):
        """Test case for cmv 14 method with negative NUMPOINTS"""

        numPoints = -6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        E_PTS = 1
        F_PTS = 1
        area1 = 0.5
        area2 = 2.5
        self.assertFalse(CMV.cmv14(numPoints, points, E_PTS, F_PTS, area1, area2))

