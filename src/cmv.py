import math

import numpy as np

""""Conditions Met Vector (CMV)"""

class CMV:
    """"Conditions Met Vector (CMV) class.

    :ivar: input: The input file
    :type: input: dict.
    :ivar: NUMPOINTS: Number of data points.
    :type: NUMPOINTS: int
    :ivar: POINTS: 2Darray containing the coordinates of data points.
    :type: POINTS: float
    :ivar: LENGTH1: The length of a distance.
    :type: LENGTH1: float
    :ivar: RADIUS1: Radius of a circle.
    :type: RADIUS1: float
    :ivar: EPSILON: Deviation from PI.
    :type: EPSILON: float
    :ivar: AREA1: Area of a triangle.
    :type: AREA1: float
    :ivar: Q_PTS: The number of consecutive data points.
    :type: Q_PTS: int
    :ivar: QUADS: Number of quadrants.
    :type: QUADS: int
    :ivar: DIST: A distance.
    :type: DIST: float
    :ivar: N_PTS: Number of consecutive points.
    :type: N_PTS: int
    :ivar: K_PTS: Number of consecutive points.
    :type: K_PTS: int
    :ivar: A_PTS: Number of consecutive points.
    :type: A_PTS: int
    :ivar: B_PTS: Number of consecutive points.
    :type: B_PTS: int
    :ivar: C_PTS: Number of consecutive points.
    :type: C_PTS: int
    :ivar: D_PTS: Number of consecutive points.
    :type: D_PTS: int
    :ivar: E_PTS: Number of consecutive points.
    :type: E_PTS: int
    :ivar: F_PTS: Number of consecutive points.
    :type: F_PTS: int
    :ivar: G_PTS: Number of consecutive points.
    :type: G_PTS: int
    :ivar: LENGTH2: The length of a distance.
    :type: LENGTH2: float
    :ivar: RADIUS2: Radius of a circle.
    :type: RADIUS2: float
    :ivar: AREA2: Area of a triangle.
    :type: AREA2: float
    """

    def __init__(self, input):
        """"Initializing the object.

        :param input: The input file.
        :type: input: dict.
        """

        self.input = input
        self.NUMPOINTS = input['NUMPOINTS']
        self.POINTS = input['POINTS']
        self.LENGTH1 = input['PARAMETERS']['LENGTH1']
        self.RADIUS1 = input['PARAMETERS']['RADIUS1']
        self.EPSILON = input['PARAMETERS']['EPSILON']
        self.AREA1 = input['PARAMETERS']['AREA1']
        self.Q_PTS = input['PARAMETERS']['Q_PTS']
        self.QUADS = input['PARAMETERS']['QUADS']
        self.DIST = input['PARAMETERS']['DIST']
        self.N_PTS = input['PARAMETERS']['N_PTS']
        self.K_PTS = input['PARAMETERS']['K_PTS']
        self.A_PTS = input['PARAMETERS']['A_PTS']
        self.B_PTS = input['PARAMETERS']['B_PTS']
        self.C_PTS = input['PARAMETERS']['C_PTS']
        self.D_PTS = input['PARAMETERS']['D_PTS']
        self.E_PTS = input['PARAMETERS']['E_PTS']
        self.F_PTS = input['PARAMETERS']['F_PTS']
        self.G_PTS = input['PARAMETERS']['G_PTS']
        self.LENGTH2 = input['PARAMETERS']['LENGTH2']
        self.RADIUS2 = input['PARAMETERS']['RADIUS2']
        self.AREA2 = input['PARAMETERS']['AREA2']

    @staticmethod
    def cmv0(POINTS, LENGTH1):
        """"Check if there exists at least one set of consecutive data points that
        are a distance greater than LENGTH1 apart.

        :param POINTS: 2Darray containing the coordinates of data points.
        :type POINTS: float
        :param LENGTH1: Float length greater than or equal to 0
        :type LENGTH1: float
        :returns: True if one set of consecutive data points are found that fulfills the requirement.
        :rtype: bool
        """
        if not (0 <= LENGTH1):
            return False
        NUMPOINTS = len(POINTS)
        for i in range(NUMPOINTS - 1):
            if np.sqrt(((POINTS[i][0] - POINTS[i+1][0])**2) + ((
            POINTS[i][1] - POINTS[i+1][1])**2)) > LENGTH1:
                return True
        return False

    @staticmethod
    def cmv1(NUMPOINTS, POINTS, RADIUS1):
        """Checking if there exists at least one set of three consecutive data points that cannot all be contained
        within or on a circle of radius RADIUS1.

        :param NUMPOINTS: Number of data points.
        :type NUMPOINTS: int
        :param POINTS: 2Darray containing the coordinates of data points.
        :type POINTS: 2Darray(float)
        :param RADIUS1: Radius of a circle.
        :type RADIUS1: float
        :returns: True if the method's condition is satisfied otherwise return false.
        :rtype: bool
        """
        if not (0 <= RADIUS1):
            return False
        for i in range(NUMPOINTS - 3):
            dis_1_2 = math.sqrt(
                (POINTS[i][0] - POINTS[i + 1][0]) ** 2 + (POINTS[i][1] - POINTS[i + 1][1]) ** 2)
            dis_2_3 = math.sqrt(
                (POINTS[i + 1][0] - POINTS[i + 2][0]) ** 2 + (POINTS[i + 1][1] - POINTS[i + 2][1]) ** 2)
            dis_3_1 = math.sqrt(
                (POINTS[i + 2][0] - POINTS[i][0]) ** 2 + (POINTS[i + 2][1] ** 2 - POINTS[i][1]) ** 2)
            max_radius = max(dis_1_2, dis_2_3, dis_3_1) / 2
            if max_radius > RADIUS1:
                return True
        return False

    @staticmethod
    def cmv2(POINTS, EPSILON):
        """Checking if there exists at least one set of three consecutive data points which form an angle.

        :param POINTS: 2Darray containing the coordinates of data points.
        :type POINTS: 2Darray(float)
        :param EPSILON: Deviation from PI.
        :type EPSILON: float
        :returns: True if the method's condition is satisfied otherwise return false.
        :rtype: bool
        """
        PI = math.pi
        if not (0 <= EPSILON < PI):
            return False
        for i in range(len(POINTS) - 2):
            point_1_x = POINTS[i][0]
            point_1_y = POINTS[i][1]
            point_2_x = POINTS[i+1][0]
            point_2_y = POINTS[i+1][1]
            point_3_x = POINTS[i+2][0]
            point_3_y = POINTS[i+2][1]
            if not(point_1_x == point_2_x and point_1_y == point_2_y) and not(point_3_x == point_2_x and point_3_y == point_2_y):
                u = [point_1_x - point_2_x, point_1_y - point_2_y]
                v = [point_3_x - point_2_x, point_3_y - point_2_y]
                angle = np.arccos(np.dot(u/np.linalg.norm(u), v/np.linalg.norm(v)))
                if (angle < PI-EPSILON) or (angle > PI+EPSILON):
                    return True
        return False

    @staticmethod
    def cmv3(NUMPOINTS, POINTS, AREA1):
        """ Checking if there exists at least one set of three consecutive data points that are the vertices of a triangle with area greater than AREA1.
        :param NUMPOINTS: The number of planar data points.
        :type NUMPOINTS: int
        :param POINTS: 2Darray containing the coordinates of data points.
        :type POINTS: float
        :param AREA1: The area
        :type AREA1: float
        :returns: True if area of three consecutive points is greater than AREA1. Otherwise False
        :rtype: bool
        """
        
        if not (0 <= AREA1):
            return False
        for i in range(NUMPOINTS-2):
            ax = POINTS[i][0]
            ay = POINTS[i][1]
            bx = POINTS[i+1][0]
            by = POINTS[i+1][1]
            cx = POINTS[i+2][0]
            cy = POINTS[i+2][1]

            TRIANGLEAREA = abs((ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))/2)
            if TRIANGLEAREA > AREA1:
                return True
        return False

    @staticmethod
    def cmv4(NUMPOINTS, POINTS, Q_PTS, QUADS):
        """
        Checking that there exists at least one set of Q_PTS consecutive data points that lie in more than QUADS quadrants.
        
        :param NUMPOINTS: Number of data points.
        :type NUMPOINTS: int
        :param POINTS: 2Darray containing the coordinates of data points.
        :type POINTS: 2Darray(float)
        :param Q_PTS: The number of consecutive data points.
        :type Q_PTS: int
        :param QUADS: Number of quadrants
        :type QUADS: int
        :returns: True is a set of Q_PTS lie in more than QUAD quadrants and 1<= QUADS <=3 else False
        """
        if not (2 <= Q_PTS <= NUMPOINTS) or not (1 <= QUADS <= 3):
            return False
        quadrant = [(0, 0), (-1, 0), (0, -1), (1, 0)]
        last_quad = None
        for i in range(NUMPOINTS - 1):
            if POINTS[i][0] >= 0:
                if POINTS[i][1] >= 0:
                    if last_quad != quadrant[0]:
                        if i != 0:
                            return True
                    else:
                        last_quad = quadrant[0]
                else:
                    if last_quad != quadrant[3]:
                        if i != 0:
                            return True
                        else:
                            last_quad = quadrant[3]
                    else:
                        last_quad = quadrant[3]

            if POINTS[i][0] < 0:
                if POINTS[i][1] >= 0:
                    if last_quad != quadrant[1]:
                        if i != 0:
                            return True
                        else:
                            last_quad = quadrant[1]
                    else:
                        last_quad = quadrant[1]
                else:
                    if last_quad != quadrant[2]:
                        if i != 0:
                            return True
                        else:
                            last_quad = quadrant[2]
                    else:
                        last_quad = quadrant[2]
        
        return False


    @staticmethod
    def cmv5(NUMPOINTS, POINTS):
        """Checking if there are at least one set of consecutive data points where Xj - Xi < 0.

        :param NUMPOINTS: Number of data points.
        :type NUMPOINTS: int
        :param POINTS: 2Darray containing the coordinates of data points.
        :type POINTS: float
        :returns: True if condition Xj - Xi < 0 is satisfied, otherwise return False.
        :rtype: bool
        """

        for i in range(NUMPOINTS - 2):
            for j in range(1, NUMPOINTS - 1):
                if (POINTS[j][0] - POINTS[i][0]) < 0:
                    return True
        return False

    @staticmethod
    def cmv6(NUMPOINTS, POINTS, N_PTS, DIST):
        """
        Checking if there exists at least one set of N_PTS consecutive data points such that at least
        one of the points lies a distance greater than DIST from the line joining the first and last of these
        N_PTS points.
        :param: NUMPOINTS: Number of data points.
        :type: NUMPOINTS: int
        :param: POINTS: 2Darray containing the coordinates of data points.
        :type: POINTS: 2Darray (floats)
        :param: N_PTS: Number of consecutive points.
        :type: N_PTS: int
        :param: DIST: A distance
        :type: DIST: float
        :returns: True if 3 <= N_PTS <= NUMPOINTS and 0 <= DIST else False
        :rtype: bool
        """
        if NUMPOINTS < 3:
            return False
        if NUMPOINTS < N_PTS or DIST <= 0:
            return False
        for i in range(0, NUMPOINTS - N_PTS):
            if POINTS[i][0] == POINTS[i + N_PTS - 1][0] and POINTS[i][1] == POINTS[i + N_PTS - 1][1]:
                for j in range(1, i + N_PTS - 1):
                    if math.sqrt((POINTS[i][0] - POINTS[i + j][0]) ** 2 + (POINTS[i][1] - POINTS[i + j][1]) ** 2) > DIST:
                        return True
            else:
                for j in range(1, N_PTS):
                    side_1 = math.sqrt(
                            (POINTS[i + N_PTS - 1][0] - POINTS[i][0]) ** 2 + (POINTS[i + N_PTS - 1][1] - POINTS[i][1]) ** 2)
                    side_2 = math.sqrt((POINTS[i + j][0] - POINTS[i][0]) ** 2 + (POINTS[i + j][1] - POINTS[i][1]) ** 2)
                    side_3 = math.sqrt((POINTS[i + N_PTS - 1][0] - POINTS[i + j][0]) ** 2 + (
                            POINTS[i + N_PTS - 1][1] - POINTS[i + j][1]) ** 2)
                    if side_1 == 0.0 or side_2 == 0.0 or side_3 == 0.0:
                        continue   
                    cos_angle = math.acos((side_1 ** 2 + side_2 ** 2 - side_3 ** 2) / (2 * side_1 * side_2))
                    comparison_distance = math.sin(cos_angle) * side_2

                    if (comparison_distance > DIST):
                            return True
        return False

    @staticmethod
    def cmv7(NUMPOINTS, POINTS, K_PTS, LENGTH1):
        """"Check if there exists at least one set of two data points separated by K_PTS consecutive intervening
        points that are a distance greater than LENGTH1 apart.

        :param NUMPOINTS: Number of data points.
        :type NUMPOINTS: int
        :param POINTS: 2Darray containing the coordinates of data points.
        :type POINTS: float
        :param K_PTS: The number of int points.
        :type K_PTS: int
        :param LENGTH1: Float length greater or equal to 0.
        :type LENGTH1: float
        :returns: True if conditions are met, otherwise False.
        :rtype: bool
        """

        if (not (1 <= K_PTS) and (not(K_PTS <= NUMPOINTS - 2))) or NUMPOINTS < 3:
            return False
        else:
            for i in range(NUMPOINTS - K_PTS - 1):
                if((np.sqrt(((POINTS[i][0] - POINTS[i + K_PTS + 1][0])**2) + 
                ((POINTS[i][1] - POINTS[i + K_PTS + 1][1])**2))) > LENGTH1):
                    return True
        return False

    @staticmethod
    def cmv8(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1):
        """
        :param NUMPOINTS: Number of data points.
        :type NUMPOINTS: int
        :param POINTS: 2Darray containing the coordinates of data points.
        :type POINTS: float
        :param A_PTS: The number of int points.
        :type A_PTS: int
        :param B_PTS: The number of int points.
        :type B_PTS: int
        :param RADIUS1: Radius of a circle.
        :type RADIUS1: float
        :returns: True if conditions are met, otherwise False.
        :rtype: bool
        """
        
        if (NUMPOINTS < 5):
            return False
        if (not(1 <= A_PTS)):
            return False
        if (not(1 <= B_PTS)):
            return False
        if (not(A_PTS + B_PTS <= NUMPOINTS-3)):
            return False

        i = 0
        while (i + A_PTS + B_PTS + 2 < NUMPOINTS):
            point_1 = (POINTS[i][0], POINTS[i][1])
            point_2 = (POINTS[i + A_PTS + 1][0], POINTS[i + A_PTS + 1][1])
            point_3 = (POINTS[i + A_PTS + B_PTS + 2][0], POINTS[i + A_PTS + B_PTS + 2][1])
            
            distance1 = math.dist(point_1, point_2)
            distance2 = math.dist(point_2, point_3)
            distance3 = math.dist(point_3, point_1)

            s = (distance1+distance2+distance3)/2
            area = math.sqrt(s * (s - distance1) * (s - distance2) * (s - distance3))
            circradius = distance1 * distance2 * distance3 / (4 * area)

            if (circradius > RADIUS1):
                return True
            i = i + 1

        return False
            
    @staticmethod
    def cmv9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON):
        """Checking if there exists at least one set of three data points separated by exactly C_PTS and D_PTS
        consecutive intervening points, respectively, that form an angle.

        :param NUMPOINTS: The number of planar data points.
        :type NUMPOINTS: int
        :param POINTS: 2Darray containing the coordinates of data points.
        :type POINTS: 2Darray(float)
        :param C_PTS: The number of int points.
        :type C_PTS: int
        :param D_PTS: The number of int points.
        :type D_PTS: int
        :param EPSILON: Deviation from PI.
        :type EPSILON: float
        :returns: True if the method's condition is satisfied otherwise return false.
        :rtype: bool
        """
        PI = math.pi
        if (not (1 <= C_PTS)) or (not (1 <= D_PTS)) or (not (C_PTS + D_PTS <= NUMPOINTS - 3)) or NUMPOINTS < 5:
            return False
        i = 0
        while (i + C_PTS + D_PTS + 2 < NUMPOINTS):
            point_1_x = POINTS[i][0]
            point_1_y = POINTS[i][1]
            point_2_x = POINTS[i + C_PTS + 1][0]
            point_2_y = POINTS[i + C_PTS + 1][1]
            point_3_x = POINTS[i + C_PTS + D_PTS + 2][0]
            point_3_y = POINTS[i + C_PTS + D_PTS + 2][1]
            if not (point_1_x == point_2_x and point_1_y == point_2_y) and not (
                    point_3_x == point_2_x and point_3_y == point_2_y):
                u = [point_1_x - point_2_x, point_1_y - point_2_y]
                v = [point_3_x - point_2_x, point_3_y - point_2_y]
                angle = np.arccos(np.dot(u / np.linalg.norm(u), v / np.linalg.norm(v)))
                if (angle < PI - EPSILON) or (angle > PI + EPSILON):
                    return True
            i += 1
        return False

    @staticmethod
    def cmv10(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1):
        """Checking if there exists at least one set of three data points separated by exactly E_PTS and F_PTS consecutive
         intervening points, respectively, that are the vertices of a triangle with area greater than AREA1.
         
        :param NUMPOINTS: The number of planar data points.
        :type NUMPOINTS: int
        :param POINTS: 2Darray containing the coordinates of data points.
        :type POINTS: 2Darray(float)
        :param E_PTS: The number of int points.
        :type E_PTS: int
        :param F_PTS: The number of int points.
        :type F_PTS: int
        :param AREA1: The area.
        :type AREA1: float
        :returns: True if the method's condition is satisfied otherwise return false.
        :rtype: bool
        """
        if (not (1 <= E_PTS)) or (not (1 <= F_PTS)) or (not (E_PTS + F_PTS <= NUMPOINTS - 3)) or NUMPOINTS < 5:
            return False
        i = 0
        while (i + E_PTS + F_PTS + 2 < NUMPOINTS):
            point_1_x = POINTS[i][0]
            point_1_y = POINTS[i][1]
            point_2_x = POINTS[i + E_PTS + 1][0]
            point_2_y = POINTS[i + E_PTS + 1][1]
            point_3_x = POINTS[i + E_PTS + F_PTS + 2][0]
            point_3_y = POINTS[i + E_PTS + F_PTS + 2][1]
            triangle_area = abs((point_1_x*(point_2_y-point_3_y) + point_2_x*(point_3_y-point_1_y) + point_3_x*(point_1_y-point_2_y))/2)
            if triangle_area > AREA1:
                return True
            i += 1
        return False
    
    @staticmethod    
    def cmv12(NUMPOINTS, POINTS, K_PTS, LENGTH1, LENGTH2):
        """Checking if there exists at least one set of two data points seperated by exactly K_PTS consecutive intervening points.
        The distance of these points are greater than the LENGTH1 apart. 
        In addition it checks if there also exist at least one set of two data points separated by exactly K_PTS
        consecutive intervening points with a distance less than LENGTH2 apart from each other. 

        :param K_PTS: The number of int points
        :type K_PTS: int
        :param LENGTH1: The length of a distance
        :type LENGTH1: float
        :param LENGTH2: The lenght of a distance
        :tyoe LENGTH2: float
        :returns: True if both the conditions in the method are satisfied else false.
        :rtype: bool 
        """
        if NUMPOINTS < 3 or LENGTH2 <= 0 or K_PTS < 0:
            return False
        
        length1_check = False
        length2_check = False
        
        for i in range(NUMPOINTS - K_PTS - 1):
            distance = math.sqrt((POINTS[i][0] - POINTS[i + K_PTS + 1][0]) ** 2 + (POINTS[i][1] - POINTS[i + K_PTS + 1][1]) ** 2)
            if distance > LENGTH1:
                length1_check = True
            if distance > LENGTH2:
                length2_check = True
        
        if length1_check and length2_check:
            return True
        else:
            return False

    @staticmethod
    def cmv13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2):
        """ Checking if both conditions are satisfied
        1)There exists at least one set of three data points, separated by exactly A PTS and B PTS
         consecutive intervening points, respectively, that cannot be contained within or on a circle of
         radius RADIUS1.
        2)There exists at least one set of three data points (which can be the same or different from
         the three data points just mentioned) separated by exactly A PTS and B PTS consecutive
         intervening points, respectively, that can be contained in or on a circle of radius RADIUS2.

        :param NUMPOINTS: Number of data points.
        :type NUMPOINTS: int
        :param POINTS: 2Darray containing the coordinates of data points.
        :type POINTS: 2Darray(float)
        :param A_PTS: The number of int points.
        :type A_PTS: int
        :param B_PTS: The number of int points.
        :type B_PTS: int
        :param RADIUS1: Radius of a circle.
        :type RADIUS1: float
        :param RADIUS2: Radius of a circle.
        :type RADIUS2: float
        :returns: True if the method's conditions are satisfied otherwise return false.
        :rtype: bool
        """
        if NUMPOINTS < 5 or not (0 <= RADIUS2):
            return False
        i = 0
        con_1 = False
        con_2 = False
        while i + A_PTS + B_PTS + 2 < NUMPOINTS:
            point_1_x = POINTS[i][0]
            point_1_y = POINTS[i][1]
            point_2_x = POINTS[i + A_PTS + 1][0]
            point_2_y = POINTS[i + A_PTS + 1][1]
            point_3_x = POINTS[i + A_PTS + B_PTS + 2][0]
            point_3_y = POINTS[i + A_PTS + B_PTS + 2][1]
            dis_1_2 = math.sqrt((point_1_x - point_2_x) ** 2 + (point_1_y - point_2_y) ** 2)
            dis_2_3 = math.sqrt((point_2_x - point_3_x) ** 2 + (point_2_y - point_3_y) ** 2)
            dis_3_1 = math.sqrt((point_3_x - point_1_x) ** 2 + (point_3_y - point_1_y) ** 2)
            max_radius = max(dis_1_2, dis_2_3, dis_3_1) / 2
            if max_radius > RADIUS1:
                con_1 = True
            if max_radius <= RADIUS2:
                con_2 = True
            if con_1 and con_2:
                return True
            i = i + 1
        return False

    @staticmethod
    def cmv14(NUMPOINTS, POINTS, E_PTS, F_PTS, AREA1, AREA2):
        """ Checking if both conditions are satisfied
        1)There exists at least one set of three data points, separated by exactly E PTS and F PTS consecutive
         intervening points, respectively, that are the vertices of a triangle with area greater than AREA1.
        2)There exist three data points (which can be the same or different
         from the three data points just mentioned) separated by exactly E PTS and F PTS consecutive
         intervening points, respectively, that are the vertices of a triangle with area less than
         AREA2.

        :param NUMPOINTS: Number of data points.
        :type NUMPOINTS: int
        :param POINTS: 2Darray containing the coordinates of data points.
        :type POINTS: 2Darray(float)
        :param E_PTS: The number of int points.
        :type E_PTS: int
        :param F_PTS: The number of int points.
        :type F_PTS: int
        :param AREA1: Area of a triangle.
        :type AREA1: float
        :param AREA2: Area of a triangle.
        :type AREA2: float
        :returns: True if the method's conditions are satisfied otherwise return false.
        :rtype: bool
        """
        if NUMPOINTS < 5 or not (0 <= AREA2):
            return False
        i = 0
        con_1 = False
        con_2 = False
        while i + E_PTS + F_PTS + 2 < NUMPOINTS:
            point_1_x = POINTS[i][0]
            point_1_y = POINTS[i][1]
            point_2_x = POINTS[i + E_PTS + 1][0]
            point_2_y = POINTS[i + E_PTS + 1][1]
            point_3_x = POINTS[i + E_PTS + F_PTS + 2][0]
            point_3_y = POINTS[i + E_PTS + F_PTS + 2][1]
            triangle_area = abs((point_1_x * point_2_y - point_1_x * point_3_y +
                                 point_2_x * point_3_y - point_2_x * point_1_y +
                                 point_3_x * point_1_y - point_3_x * point_2_y)) / 2
            if triangle_area > AREA1:
                print("1")
                con_1 = True
            if triangle_area < AREA2:
                print("2")
                con_2 = True
            if con_1 and con_2:
                return True
            i = i + 1
        return False

    def calc_CMV(self):
        CMV = [
            self.cmv0(self.POINTS, self.LENGTH1),
            self.cmv1(self.NUMPOINTS, self.POINTS, self.RADIUS1),
            self.cmv2(self.POINTS, self.EPSILON),
            self.cmv3(self.NUMPOINTS, self.POINTS, self.AREA1),
            self.cmv4(self.NUMPOINTS, self.POINTS, self.Q_PTS, self.QUADS),
            self.cmv5(self.NUMPOINTS, self.POINTS),
            self.cmv6(self.NUMPOINTS, self.POINTS, self.N_PTS, self.DIST),
            self.cmv9(self.NUMPOINTS, self.POINTS, self.C_PTS, self.D_PTS, self.EPSILON),
            self.cmv12(self.NUMPOINTS, self.POINTS, self.K_PTS, self.LENGTH1, self.LENGTH2),
            self.cmv13(self.NUMPOINTS, self.POINTS, self.A_PTS, self.B_PTS, self.RADIUS1, self.RADIUS2),
            self.cmv14(self.NUMPOINTS, self.POINTS, self.AREA1, self.AREA2, self.E_PTS, self.F_PTS),
        ]
        return CMV
