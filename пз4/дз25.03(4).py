import numpy as np

def lu_decomposition(A):
    n = A.shape[0]
    L = np.zeros_like(A)
    U = np.zeros_like(A)
    for i in range(n):
        # Устанавливаем диагональные элементы U
        U[i, i] = 1
        for j in range(i, n):
            L[j, i] = A[j, i] - np.dot(L[j, :i], U[:i, i])
        for j in range(i + 1, n):
            U[i, j] = (A[i, j] - np.dot(L[i, :i], U[:i, j])) / L[i, i]
    return L, U

def forward(L, b):
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])
    return y

def backward(U, y):
    n = len(y)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

def lu_solve(A, b):
    L, U = lu_decomposition(A)
    y = forward(L, b)
    x = backward(U, y)
    return x

A = np.array([[2, 1, -1],
                [-3, -1, 2],
                [-2, 1, 2]])
b = np.array([8, -11, -3], dtype=float)
answer = lu_solve(A, b)
print("Решение системы уравнений:", answer)
