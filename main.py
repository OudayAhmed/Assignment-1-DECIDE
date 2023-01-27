import math
import numpy as np

# constant
PI = math.pi

# Type Declarations
COORDINATE = np.empty([100, ], dtype=float)
CONNECTORS = np.zeros([15, 15])
BMATRIX = np.zeros([15, 15], dtype=bool)
VECTOR = np.empty([15, ], dtype=bool)

# Inputs to the DECIDE() function
LENGTH1 = float
RADIUS1 = float
EPSILON = float
AREA1 = float
Q_PTS = int
QUADS = int
DIST = float
N_PTS = int
K_PTS = int
A_PTS = int
B_PTS = int
C_PTS = int
D_PTS = int
E_PTS = int
F_PTS = int
G_PTS = int
LENGTH2 = float
RADIUS2 = float
AREA2 = float

# Global variable declarations
LAUNCH = False
CMV = VECTOR


def CMV_0(POINTS):
    if not (0 <= LENGTH1):
        return False
    NUMPOINTS = len(POINTS)
    for i in range(NUMPOINTS - 1):
        if math.sqrt((POINTS[i][0] ** 2 - POINTS[i + 1][0] ** 2) + (
                POINTS[i + 1][1] ** 2 - POINTS[i + 1][1] ** 2)) > LENGTH1:
            return True
    return False


def CMV_2(POINTS, EPSILON, PI):
    if not (0 <= EPSILON < PI):
        return False
    for i in range(len(POINTS) - 2):
        point_1_x = POINTS[i][0]
        point_1_y = POINTS[i][1]
        point_2_x = POINTS[i + 1][0]
        point_2_y = POINTS[i + 1][1]
        point_3_x = POINTS[i + 2][0]
        point_3_y = POINTS[i + 2][1]
        if not (point_1_x == point_2_x and point_1_y == point_2_y) or not (
                point_3_x == point_2_x and point_3_y == point_2_y):
            u = [point_1_x - point_2_x, point_1_y - point_2_y]
            v = [point_3_x - point_2_x, point_3_y - point_2_y]
            angle = np.arccos(np.dot(u / np.linalg.norm(u), v / np.linalg.norm(v)))
            if (angle < PI - EPSILON) or (angle > PI + EPSILON):
                return True
    return False


def CMV_5(POINTS):
    NUMPOINTS = len(POINTS)
    for i in range(NUMPOINTS - 2):
        for j in range(1, NUMPOINTS - 1):
            if (POINTS[j] - POINTS[i]) < 0:
                return True
    return False


def CMV_6(POINTS, N_PTS, DIST):
    NUMPOINTS = len(POINTS)
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
                    cos_angle = math.acos((side_1 ** 2 + side_2 ** 2 - side_3 ** 2) / (2 * side_1 * side_2))
                    comparison_distance = math.sin(cos_angle) * side_2

                    if (comparison_distance > DIST):
                        return True
    return False


def CMV_4(POINTS, NUMPOINTS, Q_PTS, QUADS):
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


def CMV_9(POINTS, C_PTS, D_PTS, NUMPOINTS, PI, EPSILON):
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


def CMV_1(POINTS, NUMPOINTS):
    if not (0 <= RADIUS1):
        return False
    for i in range(NUMPOINTS - 3):
        dis_1_2 = math.sqrt((POINTS[i][0] ** 2 - POINTS[i + 1][0] ** 2) + (POINTS[i][1] ** 2 - POINTS[i + 1][1] ** 2))
        dis_2_3 = math.sqrt((POINTS[i + 1][0] ** 2 - POINTS[i + 2][0] ** 2) + (POINTS[i + 1][1] ** 2 - POINTS[i + 2][1] ** 2))
        dis_3_1 = math.sqrt((POINTS[i + 2][0] ** 2 - POINTS[i][0] ** 2) + (POINTS[i + 2][1] ** 2 - POINTS[i][1] ** 2))
        max_radius = max(dis_1_2, dis_2_3, dis_3_1) / 2
        if max_radius > RADIUS1:
            return True
    return False


def CMV_13(POINTS, NUMPOINTS, A_PTS, B_PTS):
    if NUMPOINTS < 5 or not(0 <= RADIUS2):
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

def DECIDE():
    pass
