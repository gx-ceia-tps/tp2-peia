import numpy as np
import matplotlib.pyplot as plt
# Datos
X = np.array([0, 5, 10, 15, 24])
Y = np.array([10, 18, 151, 219, 492])

n = len(X)
X_sum = np.sum(X)
X2_sum = np.sum(X**2)
X3_sum = np.sum(X**3)
X4_sum = np.sum(X**4)
Y_sum = np.sum(Y)
XY_sum = np.sum(X * Y)
X2Y_sum = np.sum(X**2 * Y)

A = np.array([
    [1, X_sum, X2_sum],
    [X_sum, X2_sum, X3_sum],
    [X2_sum, X3_sum, X4_sum]
])

B = np.array([Y_sum, XY_sum, X2Y_sum])
#    [a]
# A  [b]  =   B
#    [c]
a, b, c = np.linalg.solve(A, B)

print(f"a = {a}, b = {b}, c = {c}")

X_fit = np.linspace(0, 24, 100)
Y_fit = a + b * X_fit + c * X_fit**2
plt.scatter(X, Y, color='blue', label='Datos')
plt.plot(X_fit, Y_fit, color='red', label='Modelo')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Ajuste de mínimos cuadrados')
plt.show()
