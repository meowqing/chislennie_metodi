import numpy as np

def gauss_jordan(A, b):
    n = len(b)
    # Объединяем матрицу A и вектор b в расширенную матрицу
    Ab = np.hstack([A, b.reshape(-1, 1)])
    for i in range(n):
        Ab[i] = Ab[i] / Ab[i][i]
        for j in range(n):
            if j != i:
                Ab[j] -= Ab[j][i] * Ab[i]
    return Ab[:, -1]

A = np.array([[2, 1, -1],
                [-3, -1, 2],
                [-2, 1, 2]])
b = np.array([8, -11, -3])
answer = gauss_jordan(A, b)
print("Решение системы уравнений:", answer)
