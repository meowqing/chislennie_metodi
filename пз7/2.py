import numpy as np


def rotation_method(A, tol=1e-3, max_iterations=100):
    n = A.shape[0]
    for _ in range(max_iterations):
        # Находим индексы элемента, который нужно обрабатывать
        p, q = np.unravel_index(np.argmax(np.abs(A - np.diag(np.diag(A)))), A.shape)
        if np.abs(A[p, q]) < tol:
            break

        # Вычисляем угол вращения
        theta = 0.5 * np.arctan2(2 * A[p, q], A[q, q] - A[p, p])

        # Создаем матрицу вращения
        B = np.eye(n)
        B[p, p] = np.cos(theta)
        B[p, q] = -np.sin(theta)
        B[q, p] = np.sin(theta)
        B[q, q] = np.cos(theta)

        A = B.T @ A @ B

    # Собственные значения находятся на диагонали матрицы A
    eigenvalues = np.diag(A)

    # Собственные векторы — столбцы матрицы B
    eigenvectors = B

    return eigenvalues, eigenvectors


# Пример
A = np.array([[4, 2], [2, 3]])
eigenvalues, eigenvectors = rotation_method(A)
print("Собственные значения:", eigenvalues)
print("Собственные векторы:", eigenvectors)
