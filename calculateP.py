import numpy as np
import matplotlib.pyplot as plt

ITERATIONS = 5
P = np.zeros((ITERATIONS+1, 2, 2))


P_plus = np.array([[4, 0], [0, 4]])
P[0] = P_plus


F = np.array([[1, 0], [0, 1]])
R = np.array([[4, 0],[0, 4]])
Q = np.array([[1e-1, 0], [0, 1e-1]])
H = np.array([[1, 0],[0, 1]])
I = np.eye(2)

for iter in range(ITERATIONS):

    P_minus = F @ P_plus @ F.T + Q
    S = H @ P_minus @H.T + R
    K = P_minus @ H.T @ np.linalg.inv(S)

    P_plus = (I - K @ H) @ P_minus @ (I - K @ H).T + K @ np.linalg.inv(R) @ K.T
    P[iter+1] = P_plus

# Print all P matrices
print("All P matrices:")

plt.figure(1)
plt.grid(visible=True, which='both', color='gray', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.scatter(range(ITERATIONS), [P[iter][0,0] for iter in range(ITERATIONS)])
plt.title('Postional Variance')
plt.grid()
plt.show()