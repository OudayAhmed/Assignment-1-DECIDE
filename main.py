import math
import numpy as np

#constant
PI = math.pi



#Type Declarations
COORDINATE = np.empty([100,], dtype = float)
CONNECTORS = np.zeros([15,15])
BMATRIX = np.zeros([15,15], dtype=bool)
VECTOR = np.empty([15,], dtype = bool)

# Inputs to the DECIDE() function
LENGTH1 = float
RADIUS1 = float
EPSILON =  float
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
    NUMPOINTS = len(POINTS)
    for i in range(NUMPOINTS-1):
        if math.sqrt((POINTS[i][0]**2 - POINTS[i+1][0]**2) +  (POINTS[i+1][1]**2 - POINTS[i+1][1] ** 2)) > LENGTH1:
            return True

def CMV_2(POINTS, EPSILON, PI):
    if not (0 <= EPSILON < PI):
        raise ValueError("EPSILON must be between 0 and PI")
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


def CMV_5(POINTS):
    NUMPOINTS = len(POINTS)
    for i in range(NUMPOINTS-2):
        for j in range(1, NUMPOINTS-1):
            if (POINTS[j] - POINTS[i]) < 0:
                return True

def CMV_4(POINTS):
    NUMPOINTS = len(POINTS)
    quadrant = [(0,0),(-1,0),(0,-1),(1,0)]
    last_quad = None

    for i in range(NUMPOINTS-1):
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


def DECIDE():
    pass