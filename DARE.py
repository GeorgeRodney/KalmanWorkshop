##################################################################
#
#   Discrete Algebraic Riccati Equations
#
#   Used to arrive at a steady state covariance matrix
#
#   solve_discrete_are(a, b, q, r, e=None, s=None, balanced=True) <----- API
#
#   a = A: State transition matrix
#   b = B: Control input matrix
#   q = Q: Process noise matrix
#   r = R: Measuremtn matrix
#   e = E: State weighting matrix: default = Identity
#   s = S: State and control cross coupling matrix. defualt is ZERO
#
#   balanced: If true it helps to stabalize the calculations. 
#             I will leave this false and if the matrixes are not stable I have another problem
##################################################################

import scipy as sci
import numpy as np



