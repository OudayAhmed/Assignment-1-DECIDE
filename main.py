import math
import numpy as np

#constant
pi = math.pi



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

def DECIDE():
    pass