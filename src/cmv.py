import math

import numpy as np


class CMV:
    def __init__(self, input):
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
        if not (0 <= LENGTH1):
            return False
        NUMPOINTS = len(POINTS)
        for i in range(NUMPOINTS - 1):
            # if math.sqrt((POINTS[i][0] ** 2 - POINTS[i + 1][0] ** 2) + (
            #         POINTS[i + 1][1] ** 2 - POINTS[i + 1][1] ** 2)) > LENGTH1:
                return True
        return False

    @staticmethod
    def cmv1(NUMPOINTS, POINTS, RADIUS1):
        if not (0 <= RADIUS1):
            return False
        # for i in range(NUMPOINTS - 3):
        #     dis_1_2 = math.sqrt((POINTS[i][0] ** 2 - POINTS[i + 1][0] ** 2) + (POINTS[i][1] ** 2 - POINTS[i + 1][1] ** 2))
        #     dis_2_3 = math.sqrt(
        #         (POINTS[i + 1][0] ** 2 - POINTS[i + 2][0] ** 2) + (POINTS[i + 1][1] ** 2 - POINTS[i + 2][1] ** 2))
        #     dis_3_1 = math.sqrt((POINTS[i + 2][0] ** 2 - POINTS[i][0] ** 2) + (POINTS[i + 2][1] ** 2 - POINTS[i][1] ** 2))
        #     max_radius = max(dis_1_2, dis_2_3, dis_3_1) / 2
        #     if max_radius > RADIUS1:
        #         return True
        return False

    @staticmethod
    def cmv2(POINTS, EPSILON):
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
            if not(point_1_x == point_2_x and point_1_y == point_2_y) or not(point_3_x == point_2_x and point_3_y == point_2_y):
                u = [point_1_x - point_2_x, point_1_y - point_2_y]
                v = [point_3_x - point_2_x, point_3_y - point_2_y]
                angle = np.arccos(np.dot(u/np.linalg.norm(u), v/np.linalg.norm(v)))
                if (angle < PI-EPSILON) or (angle > PI+EPSILON):
                    return True
        return False

    @staticmethod
    def cmv3(NUMPOINTS, POINTS, AREA1):
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
        """Method for CMV5

        Input is length of array containing datapoints and datapoints.
        Check if there are at least one set of consecutive datapoints that fulfills the requirement
        Xj - Xi < 0, where Xi = Xj -1.
        If no such datapoints exist, return false.
        """

        for i in range(NUMPOINTS - 2):
            for j in range(1, NUMPOINTS - 1):
                if (POINTS[j][0] - POINTS[i][0]) < 0:
                    return True
        return False

    @staticmethod
    def cmv6(NUMPOINTS, POINTS, N_PTS, DIST):
        if NUMPOINTS < 3:
            return False
        elif N_PTS > NUMPOINTS or N_PTS > 3:
            return False
        else:
            for i in range(NUMPOINTS - N_PTS):
                if POINTS[i + N_PTS - 1][0] == POINTS[i][0] and POINTS[i - N_PTS - 1][1] == POINTS[i][1]:
                    for j in range(N_PTS - 1):
                        if math.sqrt(POINTS[i][0] * POINTS[i + j][0] + POINTS[i][1] * POINTS[i + j]) > DIST:
                            return True
                else:
                    for j in range(N_PTS - 1):
                        side_1 = math.sqrt(
                            (POINTS[i + N_PTS - 1][0] - POINTS[i][0]) ** 2 + (POINTS[i + N_PTS - 1][1] - POINTS[i][1]) ** 2)
                        side_2 = math.sqrt((POINTS[i + j][0] - POINTS[i][0]) ** 2 + (POINTS[i + j][1] - POINTS[i][1]) ** 2)
                        side_3 = math.sqrt((POINTS[i + N_PTS - 1][0] - POINTS[i + j][0]) ** 2 + (
                                POINTS[i + N_PTS - 1][1] - POINTS[i + j][1]) ** 2)
                        # cos_angle = math.acos((side_1 ** 2 + side_2 ** 2 - side_3 ** 2) / (2 * side_1 * side_2))
                        # comparison_distance = math.sin(cos_angle) * side_2

                        # if (comparison_distance > DIST):
                        #     return True
        return False

    @staticmethod
    def cmv9(NUMPOINTS, POINTS, C_PTS, D_PTS, EPSILON):
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
            if not (point_1_x == point_2_x and point_1_y == point_2_y) or not (
                    point_3_x == point_2_x and point_3_y == point_2_y):
                u = [point_1_x - point_2_x, point_1_y - point_2_y]
                v = [point_3_x - point_2_x, point_3_y - point_2_y]
                angle = np.arccos(np.dot(u / np.linalg.norm(u), v / np.linalg.norm(v)))
                if (angle < PI - EPSILON) or (angle > PI + EPSILON):
                    return True
        return False

    @staticmethod
    def cmv13(NUMPOINTS, POINTS, A_PTS, B_PTS, RADIUS1, RADIUS2):
        if NUMPOINTS < 5 or not (0 <= RADIUS2):
            return False
        i = 0
        true_cnt = 0
        while i + A_PTS + B_PTS + 2 < NUMPOINTS:
            point_1_x = POINTS[i][0]
            point_1_y = POINTS[i][1]
            point_2_x = POINTS[i + A_PTS + 1][0]
            point_2_y = POINTS[i + A_PTS + 1][1]
            point_3_x = POINTS[i + A_PTS + B_PTS + 2][0]
            point_3_y = POINTS[i + A_PTS + B_PTS + 2][1]
            dis_1_2 = math.sqrt((point_1_x ** 2 - point_2_x ** 2) + (point_1_y ** 2 - point_2_y ** 2))
            dis_2_3 = math.sqrt((point_2_x ** 2 - point_3_x ** 2) + (point_2_y ** 2 - point_3_y ** 2))
            dis_3_1 = math.sqrt((point_3_x ** 2 - point_1_x ** 2) + (point_3_y ** 2 - point_1_y ** 2))
            max_radius = max(dis_1_2, dis_2_3, dis_3_1) / 2
            if max_radius > RADIUS1:
                true_cnt += 1
            if max_radius <= RADIUS2:
                true_cnt += 1
            if true_cnt >= 2:
                return True
            i = i + 1
        return False

    @staticmethod
    def cmv14(NUMPOINTS, POINTS, AREA1, AREA2, E_PTS, F_PTS):
        if NUMPOINTS < 5 or not (0 <= AREA2):
            return False
        i = 0
        true_cnt = 0
        while i + E_PTS + F_PTS + 2 < NUMPOINTS:
            point_1_x = POINTS[i][0]
            point_1_y = POINTS[i][1]
            point_2_x = POINTS[i + E_PTS + 1][0]
            point_2_y = POINTS[i + E_PTS + 1][1]
            point_3_x = POINTS[i + E_PTS + F_PTS + 2][0]
            point_3_y = POINTS[i + E_PTS + F_PTS + 2][1]
            triangle_area = (point_1_x * point_2_y - point_1_x * point_3_y + \
                             point_2_x * point_3_y - point_2_x * point_1_y + \
                             point_3_x * point_1_y - point_3_x * point_2_y) / 2
            if triangle_area > AREA1:
                true_cnt += 1
            if triangle_area < AREA2:
                true_cnt += 1
            if true_cnt >= 2:
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
            self.cmv13(self.NUMPOINTS, self.POINTS, self.A_PTS, self.B_PTS, self.RADIUS1, self.RADIUS2),
            self.cmv14(self.NUMPOINTS, self.POINTS, self.AREA1, self.AREA2, self.E_PTS, self.F_PTS),
        ]
        return CMV