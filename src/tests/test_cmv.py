import unittest
from unittest import TestCase

from main.cmv import CMV

"""TestCMV"""

class TestCMV(TestCase):
    """"TestCMV class
    Contains all the test cases for all CMV conditions.
    """

    def test_cmv0_distance_smaller_than_length1(self):
        """Test case for CMV0 method.
        
        Checks to see if distance between two consecutive points in points array is greater than the distance of length1.
        Should return False because length1 is shorter than the distance between two consecutive points.
        """

        points = [[0.2, 0.3], [0.3, 0.4], [0.1, 0.3]]
        length1 = 0.3
        self.assertFalse(CMV.cmv0(points, length1))

    def test_cmv0_distance_greater_than_length1(self):
        """Test case for CMV0 method.
        
        Checks to see if distance between two consecutive points in points array is greater than the distance of length1.
        Should return True if conditions are met.
        """

        points = [[0.2, 0.3], [0.3, 0.4], [0.1, 0.3]]
        length1 = 0.1
        self.assertTrue(CMV.cmv0(points, length1))

    def test_cmv0_invalid_length1(self):
        """Test case for CMV0 method.
        
        Length1 is invalid input, should be larger or equal  to 0.
        Should return False because length1 is invalid.
        """

        points = [[0.2, 0.3], [0.3, 0.4], [0.1, 0.3]]
        length1 = -0.1
        self.assertFalse(CMV.cmv0(points, length1))

    def test_cmv_1_cannot_be_contained_in_radius1(self):
        """Positive test for cmv 1 method.
        
        Three consecutive points that cannot be contained within or on a circle of radius1.
        Should return True if at least one point cannot be contained.
        """

        numPoints = 4
        points = [[1, 3], [1, 1], [3, 1], [5, 2]]
        radius1 = 1.4
        self.assertTrue(CMV.cmv1(numPoints, points, radius1))

    def test_cmv_1_can_be_contained_in_radius1(self):
        """Negative test for cmv 1 method.
        Three consecutive points that can be contained within or on a circle of radius1.
        Should return False since all points can be contained.
        """

        numPoints = 4
        points = [[1, 3], [1, 1], [3, 1], [5, 2]]
        radius1 = 2
        self.assertFalse(CMV.cmv1(numPoints, points, radius1))

    def test_cmv_1_invalid_radius1(self):
        """Test case for cmv 1 method.
        
        Radius1 is invalid input, should be equal to or larger than 0.
        Should return False because radius1 is invalid input.
        """

        numPoints = 4
        points = [[1, 3], [1, 1], [3, 1], [5, 2]]
        radius1 = -1.4
        self.assertFalse(CMV.cmv1(numPoints, points, radius1))

    def test_cmv_2_angle_conditions_met(self):
        """Positive test for cmv 2 method.
        Checks to see if there is a set of three consecutive points which form an angle.
        Conditions for the angle are smaller than PI - EPSILON or larger than PI + EPSILON.
        Should return True because one of the conditions are met.
        """

        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        epsilon = 0.5
        self.assertTrue(CMV.cmv2(points, epsilon))

    def test_cmv_2_angle_conditions_not_met(self):
        """Negative test for cmv 2 method.
        Checks to see if there is a set of three consecutive points which form an angle.
        Conditions for the angle are smaller than PI - EPSILON or larger than PI + EPSILON.
        Should return False because none of the conditions are met.
        """

        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        epsilon = 3
        self.assertFalse(CMV.cmv2(points, epsilon))

    def test_cmv_2_invalid_epsilon(self):
        """Test case for cmv 2 method.
        Epsilon is invalid input, should be equal to or larger than 0.
        Should return False because epsilon is invalid input.
        """

        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        epsilon = -0.3
        self.assertFalse(CMV.cmv2(points, epsilon))

    def test_cmv_2_two_points_coincide(self):
        """Test case for cmv 2 method.
        Two of the three consecutive points in points array coincide, which makes the angle undefined.
        Should return False since the conditions for the angle are not satisfied.
        """

        points = [[0.1, 0.2], [0.1, 0.2], [0.2, 0.3]]
        epsilon = 0.5
        self.assertFalse(CMV.cmv2(points, epsilon))

    def test_cmv_3_larger_than_area1(self):
        """Positive test case for CMV3 method.
        Checks to see if three consecutive points form a triangle with an area larger than area1.
        Should return True because the area formed by the points is larger than area1.
        """

        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        numpoints = 3
        area1 = 0.01
        self.assertTrue(CMV.cmv3(numpoints, points, area1))

    def test_cmv_3_smaller_than_area1(self):
        """negative test case for CMV3 method.

        Checks to see if three consecutive points form a triangle with an area larger than area1.
        Should return False because the area formed by the points is smaller than area1.
        """

        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        numpoints = 3
        area1 = 1
        self.assertFalse(CMV.cmv3(numpoints, points, area1))

    def test_cmv_3_invalid_area(self):
        """Test case for CMV3 method.
        Checks to see if three consecutive points form a triangle with an area larger than area1.
        Should return False because area1 is an invalid input, should be equal to or larger than 0.
        """

        points = [[0.1, 0.2], [0.3, 0.1], [0.2, 0.3]]
        numpoints = 3
        area1 = -1
        self.assertFalse(CMV.cmv3(numpoints, points, area1))

    def test_cmv4_positive_result(self):
        """Positive test for cmv4 method.

        Checks to see if there exists at least one set of Q_PTS consecutive data points that lie in more than QUADS quadrants.
        Should return True because the conditions are met.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        q_pts = 2
        quads = 2
        self.assertTrue(CMV.cmv4(numpoints, points, q_pts, quads))

    def test_cmv4_negative_result(self):
        """Negative test for cmv4 method.
        Checks to see if there exists at least one set of Q_PTS consecutive data points that lie in more than QUADS quadrants.
        Should return False because the conditions are not met.
        """

        numpoints = 2
        points = [[0.1, 0.2], [0.2, 0.1]]
        q_pts = 3
        quads = 2
        self.assertFalse(CMV.cmv4(numpoints, points, q_pts, quads))

    def test_cmv4_invalid_quads_wrong_size(self):
        """Test case for cmv4 method.

        Checks to see if there exists at least one set of Q_PTS consecutive data points that lie in more than QUADS quadrants.
        Should return False because Quads is an invalid input, should be 1 <= quads <= 3.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        q_pts = 2
        quads = 4
        self.assertFalse(CMV.cmv4(numpoints, points, q_pts, quads))

    def test_cmv4_negative_qpts_greater_than_numpoints(self):
        """Test case for cmv4 method.

        Checks to see if there exists at least one set of Q_PTS consecutive data points that lie in more than QUADS quadrants.
        Should return False because q_pts is an invalid input. Should be 2 <= q_pts <= numpoints.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        q_pts = 8
        quads = 2
        self.assertFalse(CMV.cmv4(numpoints, points, q_pts, quads))

    def test_cmv5_Xj_larger_than_Xi(self):
        """Test case for CMV5 method.

        Checks to see if at least one set of two consecutive data points fulfill the condition Xj - Xi < 0.
        Another condition is i = j-1.
        Should return False because none of the points satisfy the condition.
        """

        points = [[0.2, 0.3], [0.4, 0.2], [0.5, 0.1]]
        numpoints = 3
        self.assertFalse(CMV.cmv5(numpoints, points))

    def test_cmv5_Xj_smaller_than_Xi(self):
        """Test case for CMV5 method.

        Checks to see if at least one set of two consecutive data points fulfill the condition Xj - Xi < 0.
        Another condition is i = j-1.
        Should return True because one set of the points satisfy the condition.
        """

        points = [[0.4, 0.3], [0.2, 0.2], [0.1, 0.3]]
        numpoints = 3
        self.assertTrue(CMV.cmv5(numpoints, points))

    def test_cmv5_invalid_amount_of_points(self):
        """Test case for CMV5 method.

        Checks to see if at least one set of two consecutive data points fulfill the condition Xj - Xi < 0.
        Another condition is i = j-1.
        Should return False because there has to be at least two points, but there is only one.
        """

        points = [[0.4, 0.3]]
        numpoints = 1
        self.assertFalse(CMV.cmv5(numpoints,points))

    def test_cmv7_larger_than_length1(self):
        """Positive test for CMV 7 method.

        Checks to see if there are at least one set of two data points that are a distance greater than length1.
        The points are separated by exactly k_pts consecutive intervening points.
        Should return True because length between the two points is greater than length1.
        """

        numpoints = 3
        points = [[0.1, 0.3], [0.2, 0.1], [0.3, 0.4]]
        k_pts = 1
        length1 = 0.1
        self.assertTrue(CMV.cmv7(numpoints, points, k_pts, length1))

    def test_cmv7_smaller_than_length1(self):
        """"Negative test for CMV 7 method.

        Checks to see if there are at least one set of two data points that are a distance greater than length1.
        The points are separated by exactly k_pts consecutive intervening points.
        Should return False because length between the two points is not greater than length1.
        """

        numpoints = 4
        points = [[0.3, 0.2], [0.4, 0.1], [0.2, 0.5], [0.5, 0.3]]
        k_pts = 2
        length1 = 0.4
        self.assertFalse(CMV.cmv7(numpoints, points, k_pts, length1))

    def test_cmv7_invalid_k_pts(self):
        """Test case for CMV7 method.

        Checks to see if there are at least one set of two data points that are a distance greater than length1.
        The points are separated by exactly k_pts consecutive intervening points.
        Should return False because the condition 1 <= k_pts <= numpoints - 2 is not met.
        """

        numpoints = 3
        points = [[0.1, 0.3], [0.2, 0.1], [0.3, 0.4]]
        k_pts = -1
        length1 = 0.1
        self.assertFalse(CMV.cmv7(numpoints, points, k_pts, length1))

    def test_cmv_6_greater_than_dist(self):
        """Positive test for cmv 6 method.

        Checks to see if there exists at least one set of n_pts consecutive data points where one point lies a distance greater than dist.
        If the first and last points of the n_pts are identical, then the distance to compare will be from coincident point to all other points.
        Should return True because conditions are met.
        """

        numpoints = 5
        points = [[1, 1], [5, 2], [1, 3], [1, 4], [1, 5]]
        n_pts = 3
        dist = 1
        self.assertTrue(CMV.cmv6(numpoints, points, n_pts, dist))

    def test_cmv_6_less_than_dist(self):
        """Negative test for cmv 6 method.

        Checks to see if there exists at least one set of n_pts consecutive data points where one point lies a distance greater than dist.
        If the first and last points of the n_pts are identical, then the distance to compare will be from coincident point to all other points.
        Should return False because the conditions are not met.
        """

        numpoints = 3
        points = [[1,0], [2,2], [1,1]]
        n_pts = 3
        dist = 4
        self.assertFalse(CMV.cmv6(numpoints, points, n_pts, dist))

    def test_cmv_6_negative_dist(self):
        """Negative test for cmv 6 method.

        Checks to see if there exists at least one set of n_pts consecutive data points where one point lies a distance greater than dist.
        If the first and last points of the n_pts are identical, then the distance to compare will be from coincident point to all other points.
        Should return False because dist is invalid input, should be equal to or greater than 0.
        """

        numpoints = 5
        points = [[1, 1], [5, 2], [1, 3], [1, 4], [1, 5]]
        n_pts = 3
        dist = -1
        self.assertFalse(CMV.cmv6(numpoints, points, n_pts, dist))

    def test_cmv_6_negative_npts_greater_than_numpoints(self):
        """Negative test for cmv 6 method.

        Checks to see if there exists at least one set of n_pts consecutive data points where one point lies a distance greater than dist.
        If the first and last points of the n_pts are identical, then the distance to compare will be from coincident point to all other points.
        Should return False because n_pts in invalid input, the conditions are 3 <= n_pts <= numpoints.
        """

        numpoints = 5
        points = [[1, 1], [5, 2], [1, 3], [1, 4], [1, 5]]
        n_pts = 7
        dist = 1
        self.assertFalse(CMV.cmv6(numpoints, points, n_pts, dist))

    def test_cmv_6_negative_low_npts(self):
        """Negative test for cmv 6 method.

        Checks to see if there exists at least one set of n_pts consecutive data points where one point lies a distance greater than dist.
        If the first and last points of the n_pts are identical, then the distance to compare will be from coincident point to all other points.
        Should return False because n_pts is invalid inpud, the conditions are 3 <= n_pts <= numpoints.
        """

        numpoints = 5
        points = [[1, 1], [5, 2], [1, 3], [1, 4], [1, 5]]
        n_pts = 2
        dist = 1
        self.assertFalse(CMV.cmv6(numpoints, points, n_pts, dist))

    def test_cmv_8_cannot_be_contained_in_radius1(self):
        """Positive test for CMV8 method.

        Checks to see if there exists at least one set of three data points separated by exactly a_pts and b_pts.
        The three points cannot be contained within or on a circle of radius1.
        Should return True because the coditions are met.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.5, 0.8], [0.3, 0.2], [0.2, 0.3], [0.3, 0.9]]
        a_pts = 1
        b_pts = 1
        radius1 = 0.1
        self.assertTrue(CMV.cmv8(numpoints, points, a_pts, b_pts, radius1))

    def test_cmv_8_can_be_contained_in_radius1(self):
        """Negative test for CMV8 method.
    
        Checks to see if there exists at least one set of three data points separated by exactly a_pts and b_pts.
        The three points cannot be contained within or on a circle of radius1.
        Should return False because the coditions are not met and the points can not be contained.
        """
    
        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.5, 0.8], [0.3, 0.2], [0.2, 0.3], [0.3, 0.9]]
        a_pts = 1
        b_pts = 1
        radius1 = 100
        self.assertFalse(CMV.cmv8(numpoints, points, a_pts, b_pts, radius1))

    def test_cmv_8_invalid_numpoints_less_than_5(self):
        """Negative test for CMV8 method.

        Checks to see if there exists at least one set of three data points separated by exactly a_pts and b_pts.
        The three points cannot be contained within or on a circle of radius1.
        Should return False because numpoints is an invalid input, the conditions is not met when numpoints < 5.
        """

        numpoints = 4
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.5, 0.8]]
        a_pts = 1
        b_pts = 1
        radius1 = 0.1
        self.assertFalse(CMV.cmv8(numpoints, points, a_pts, b_pts, radius1))

    def test_cmv_9_form_angle(self):
        """Positive test for cmv 9 method.

        Checks to see if there exists at least one set of three data points separated by exactly c_pts and d_pts consecutive intervening points.
        The points form an angle such that angle < (PI - EPSILON) or angle > (PI + EPSILON).
        Should return True because the conditions are met.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.5, 0.8], [0.3, 0.2], [0.2, 0.3], [0.3, 0.9]]
        c_pts = 1
        d_pts = 2
        epsilon = 0.5
        self.assertTrue(CMV.cmv9(numpoints, points, c_pts, d_pts, epsilon))

    def test_cmv_9_does_not_meet_conditions(self):
        """Negative test for cmv 9 method.

        Checks to see if there exists at least one set of three data points separated by exactly c_pts and d_pts consecutive intervening points.
        The points form an angle such that angle < (PI - EPSILON) or angle > (PI + EPSILON).
        Should return False because the conditions are not met.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        c_pts = 2
        d_pts = 2
        epsilon = 0.3
        self.assertFalse(CMV.cmv9(numpoints, points, c_pts, d_pts, epsilon))

    def test_cmv_9_invalid_epsilon(self):
        """Test case for cmv 9 method with negative EPSILON.

        Checks to see if there exists at least one set of three data points separated by exactly c_pts and d_pts consecutive intervening points.
        The points form an angle such that angle < (PI - EPSILON) or angle > (PI + EPSILON).
        Should return False because epsilon is invalid input.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        c_pts = 2
        d_pts = 2
        epsilon = -0.8
        self.assertFalse(CMV.cmv9(numpoints, points, c_pts, d_pts, epsilon))

    def test_cmv_9_invalid_c_pts(self):
        """Test case for cmv 9 method with negative C_PTS.

        Checks to see if there exists at least one set of three data points separated by exactly c_pts and d_pts consecutive intervening points.
        The points form an angle such that angle < (PI - EPSILON) or angle > (PI + EPSILON).
        Should return False because the conditions for c_pts is 1 <= c_pts.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        c_pts = -1
        d_pts = 2
        epsilon = 0.3
        self.assertFalse(CMV.cmv9(numpoints, points, c_pts, d_pts, epsilon))

    def test_cmv_10_area_greater_than_area1(self):
        """Positive test for cmv 10 method.

        Checks to see if there exists at least one set of three data points separated by exactly e_pts and f_pts.
        The three data points should create a triangle with an area greater than area1.
        Should return True because the area is larger than area1.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.5, 0.8], [0.3, 0.4], [0.2, 0.1], [0.5, 0.1]]
        e_pts = 1
        f_pts = 2
        area1 = 0.003
        self.assertTrue(CMV.cmv10(numpoints, points, e_pts, f_pts, area1))

    def test_cmv_10_area_smaller_than_area1(self):
        """Negative test for cmv 10 method.

        Checks to see if there exists at least one set of three data points separated by exactly e_pts and f_pts.
        The three data points should create a triangle with an area greater than area1.
        Should return False because the area is smaller than area1.
        """

        numpoints = 5
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.5, 0.8], [0.2, 0.1]]
        e_pts = 1
        f_pts = 1
        area1 = 0.009
        self.assertFalse(CMV.cmv10(numpoints, points, e_pts, f_pts, area1))

    def test_cmv_10_only_three_numpoints(self):
        """Test case for cmv 10 method with only three NUMPOINTS.

        Checks to see if there exists at least one set of three data points separated by exactly e_pts and f_pts.
        The three data points should create a triangle with an area greater than area1.
        Should return False because the conditions for numpoints is not met, numpoints cannot be smaller than 5.
        """

        numpoints = 3
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1]]
        e_pts = 1
        f_pts = 1
        area1 = 0.003
        self.assertFalse(CMV.cmv10(numpoints, points, e_pts, f_pts, area1))

    def test_cmv_10_negative_e_pts(self):
        """Test case for cmv 10 method with negative E_PTS.

        Checks to see if there exists at least one set of three data points separated by exactly e_pts and f_pts.
        The three data points should create a triangle with an area greater than area1.
        Should return False because the conditions for e_pts is not met, 1 <= e_pts.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.5, 0.8], [0.3, 0.4], [0.2, 0.1], [0.5, 0.1]]
        e_pts = -1
        f_pts = 1
        area1 = 0.002
        self.assertFalse(CMV.cmv10(numpoints, points, e_pts, f_pts, area1))

    def test_cmv_10_e_pts_and_f_pts_too_great(self):
        """Test case for cmv 10 method with E_PTS + F_PTS > NUMPOINTS - 3.

        Checks to see if there exists at least one set of three data points separated by exactly e_pts and f_pts.
        The three data points should create a triangle with an area greater than area1.
        Should return False because the condition e_pts + f_pts <= numpoints - 3 is not met.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.5, 0.8], [0.3, 0.4], [0.2, 0.1], [0.5, 0.1]]
        e_pts = 3
        f_pts = 4
        area1 = 0.001
        self.assertFalse(CMV.cmv10(numpoints, points, e_pts, f_pts, area1))

    def test_cmv_11_less_than_0(self):
        """Positive test for cmv 11 method.

        Checks to see if there exists at least one set of two data points separated by exactly g_pts consecutive intervening points.
        The condition to be met is Xj - Xi < 0 where i < j.
        Should return True because the condition is met.
        """

        numPoints = 3
        points = [[6, 3], [5, 1], [4, 1]]
        g_pts = 1
        self.assertTrue(CMV.cmv11(numPoints, points, g_pts))

    def test_cmv_11_larger_than_0(self):
        """Negative test for cmv 11 method.

        Checks to see if there exists at least one set of two data points separated by exactly g_pts consecutive intervening points.
        The condition to be met is Xj - Xi < 0 where i < j.
        Should return False because the condition is not met.
        """

        numPoints = 4
        points = [[1, 3], [1, 1], [3, 1], [5, 2]]
        g_pts = 1
        self.assertFalse(CMV.cmv11(numPoints, points, g_pts))

    def test_cmv_11_invalid_g_pts(self):
        """Negative test for cmv 11 method.

        Checks to see if there exists at least one set of two data points separated by exactly g_pts consecutive intervening points.
        The condition to be met is Xj - Xi < 0 where i < j.
        Should return False because the condition 1 <= g_pts is not met.
        g_pts is invalid input.
        """

        numPoints = 4
        points = [[1, 3], [1, 1], [3, 1], [5, 2]]
        g_pts = 0
        self.assertFalse(CMV.cmv11(numPoints, points, g_pts))

    def test_cmv_12_dist_between_length1_and_length2(self):
        """Positive test case for cmv 12.

        Checks to see if there exists at least one set of two data points, separated by exactly k_pts consecutive intervening points.
        The distance between the points are greater than length1. The distance also has to be less than length2.
        Should return True because the conditions are met.
        """

        numpoints = 3
        points = [[0.5, 0.4], [1.0, 0.7], [2.2, 0.7]]
        k_pts = 1
        length1 = 1
        length2 = 1
        self.assertTrue(CMV.cmv12(numpoints, points, k_pts, length1, length2))

    def test_cmv_12_does_not_meet_conditions(self):
        """Negative test case for cmv 12.

        Checks to see if there exists at least one set of two data points, separated by exactly k_pts consecutive intervening points.
        The distance between the points are greater than length1. The distance also has to be less than length2.
        Should return False because the conditions are not met.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        k_pts = 1
        length1 = 1
        length2 = 1
        self.assertFalse(CMV.cmv12(numpoints, points, k_pts, length1, length2))

    def test_cmv_12_invalid_numpoints(self):
        """Test case for cmv 12 method with less than 3 NUMPOINTS.

        Checks to see if there exists at least one set of two data points, separated by exactly k_pts consecutive intervening points.
        The distance between the points are greater than length1. The distance also has to be less than length2.
        Should return False because numpoints cannot be smaller than 3, making it an invalid input.
        """

        numpoints = 2
        points = [[0.1, 0.2], [0.8, 0.9]]
        k_pts = 1
        length1 = 1
        length2 = 1
        self.assertFalse(CMV.cmv12(numpoints, points, k_pts, length1, length2))

    def test_cmv_12_negative_length2(self):
        """Test case for cmv 12 method with negative LENGTH2.

        Checks to see if there exists at least one set of two data points, separated by exactly k_pts consecutive intervening points.
        The distance between the points are greater than length1. The distance also has to be less than length2.
        Should return False because the condition 0 <= length2 is not met.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        k_pts = 2
        length1 = 1
        length2 = -1
        self.assertFalse(CMV.cmv12(numpoints, points, k_pts, length1, length2))

    def test_cmv_12_negative_k_pts(self):
        """Test case for cmv 12 method with negative K_PTS.

        Checks to see if there exists at least one set of two data points, separated by exactly k_pts consecutive intervening points.
        The distance between the points are greater than length1. The distance also has to be less than length2.
        Should return False because k_pts cannot be negative, making it invalid input.
        """

        numpoints = 7
        points = [[0.1, 0.2], [0.8, 0.9], [0.3, 0.1], [0.8, 0.9], [0.3, 0.2], [0.2, 0.3], [0.8, 0.9]]
        k_pts = -1
        length1 = 1
        length2 = 1
        self.assertFalse(CMV.cmv12(numpoints, points, k_pts, length1, length2))

    def test_cmv_13_met_all_conditions(self):
        """Positive test for cmv 13 method.
        
        Checks to see if there exists at least one set of three data points, separated by exactly a_pts and b_pts.
        The three data points cannot be contained within or on a circle of radius1.
        In addition, the points can be contained within or on a circle of radius2.
        Should return True because both conditions are met.
        """

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        A_PTS = 1
        B_PTS = 1
        radius1 = 0.3
        radius2 = 2.5
        self.assertTrue(CMV.cmv13(numPoints, points, A_PTS, B_PTS, radius1, radius2))

    def test_cmv_13_negative_fail_condition_1(self):
        """Negative test of condition 1 for cmv 13 method.
        
        Checks to see if there exists at least one set of three data points, separated by exactly a_pts and b_pts.
        The three data points cannot be contained within or on a circle of radius1.
        In addition, the points can be contained within or on a circle of radius2.
        Should return False because the first condition are not met."""

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        A_PTS = 1
        B_PTS = 1
        radius1 = 2.5
        radius2 = 2.5
        self.assertFalse(CMV.cmv13(numPoints, points, A_PTS, B_PTS, radius1, radius2))

    def test_cmv_13_negative_fail_condition_2(self):
        """Negative test of condition 2 for cmv 13 method.
        
        Checks to see if there exists at least one set of three data points, separated by exactly a_pts and b_pts.
        The three data points cannot be contained within or on a circle of radius1.
        In addition, the points can be contained within or on a circle of radius2.
        Should return False because the second condition are not met.
        """

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        A_PTS = 1
        B_PTS = 1
        radius1 = 0.3
        radius2 = 0.3
        self.assertFalse(CMV.cmv13(numPoints, points, A_PTS, B_PTS, radius1, radius2))

    def test_cmv_13_negative_radius2(self):
        """Test case for cmv 13 method with negative RADIUS2.
        
        Checks to see if there exists at least one set of three data points, separated by exactly a_pts and b_pts.
        The three data points cannot be contained within or on a circle of radius1.
        In addition, the points can be contained within or on a circle of radius2.
        Should return False because the condition 0 <= radius2 is not met.
        """

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        A_PTS = 1
        B_PTS = 1
        radius1 = 0.3
        radius2 = -2.5
        self.assertFalse(CMV.cmv13(numPoints, points, A_PTS, B_PTS, radius1, radius2))

    def test_cmv_13_negative_numpoints(self):
        """Test case for cmv 13 method with negative NUMPOINTS.
        
        Checks to see if there exists at least one set of three data points, separated by exactly a_pts and b_pts.
        The three data points cannot be contained within or on a circle of radius1.
        In addition, the points can be contained within or on a circle of radius2.
        Should return False because numpoints is an invalid input, cannot be smaller than 5.
        """

        numPoints = -3
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        A_PTS = 1
        B_PTS = 1
        radius1 = 0.3
        radius2 = 2.5
        self.assertFalse(CMV.cmv13(numPoints, points, A_PTS, B_PTS, radius1, radius2))

    def test_cmv_14_conditions_met(self):
        """Positive test for cmv 14 method.
        
        Checks to see if there exists at least one set of three data points, separated by exactly e_pts and f_pts.
        The three data points create a triangle with an area greater than area1.
        In addition, the area is smaller than area2.
        Should return True because the all conditions are met.
        """

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        E_PTS = 1
        F_PTS = 1
        area1 = 0.5
        area2 = 2.5
        self.assertTrue(CMV.cmv14(numPoints, points, E_PTS, F_PTS, area1, area2))

    def test_cmv_14_negative_fail_condition_1(self):
        """Negative test of condition 1 for cmv 14 method.
        
        Checks to see if there exists at least one set of three data points, separated by exactly e_pts and f_pts.
        The three data points create a triangle with an area greater than area1.
        In addition, the area is smaller than area2.
        Should return False because the first condition is not met.
        """

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        E_PTS = 1
        F_PTS = 1
        area1 = 2.5
        area2 = 2.5
        self.assertFalse(CMV.cmv14(numPoints, points, E_PTS, F_PTS, area1, area2))

    def test_cmv_14_negative_fail_condition_2(self):
        """Negative test of condition 2 for cmv 14 method.
        
        Checks to see if there exists at least one set of three data points, separated by exactly e_pts and f_pts.
        The three data points create a triangle with an area greater than area1.
        In addition, the area is smaller than area2.
        Should return False because the second condition is not met.
        """

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        E_PTS = 1
        F_PTS = 1
        area1 = 0.5
        area2 = 0.5
        self.assertFalse(CMV.cmv14(numPoints, points, E_PTS, F_PTS, area1, area2))

    def test_cmv_14_negative_area2(self):
        """Test case for cmv 14 method with negative AREA2.
        
        Checks to see if there exists at least one set of three data points, separated by exactly e_pts and f_pts.
        The three data points create a triangle with an area greater than area1.
        In addition, the area is smaller than area2.
        Should return False because the condition 0 <= area2 is not met, making area2 invalid input.
        """

        numPoints = 6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        E_PTS = 1
        F_PTS = 1
        area1 = 0.5
        area2 = -2.5
        self.assertFalse(CMV.cmv14(numPoints, points, E_PTS, F_PTS, area1, area2))

    def test_cmv_14_negative_numpoints(self):
        """Test case for cmv 14 method with negative NUMPOINTS.
        
        Checks to see if there exists at least one set of three data points, separated by exactly e_pts and f_pts.
        The three data points create a triangle with an area greater than area1.
        In addition, the area is smaller than area2.
        Should return False because numpoints cannot be smaller than 5, making it invalid input.
        """

        numPoints = -6
        points = [[1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [5, 1]]
        E_PTS = 1
        F_PTS = 1
        area1 = 0.5
        area2 = 2.5
        self.assertFalse(CMV.cmv14(numPoints, points, E_PTS, F_PTS, area1, area2))