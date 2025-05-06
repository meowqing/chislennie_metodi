import numpy as np


def rotate(A, p, q):
    """Вращение матрицы A для обнуления элемента A[p, q]"""
    if A[p, q] == 0:
        return A

    # угол вращения
    theta = 0.5 * np.arctan2(2 * A[p, q], A[q, q] - A[p, p])
    c = np.cos(theta)
    s = np.sin(theta)

    # матрица вращения
    R = np.eye(A.shape[0])
    R[p, p] = c
    R[q, q] = c
    R[p, q] = -s
    R[q, p] = s

    return R.T @ A @ R


def count(A, max_iterations=100, tol=1e-3):
    n = A.shape[0]
    A = A.copy()
    V = np.eye(n)

    for _ in range(max_iterations):
        # Находим индексы элемента с максимальным модулем вне диагонали
        p, q = np.unravel_index(np.argmax(np.abs(A)), A.shape)

        if np.abs(A[p, q]) < tol:
            break

        # Выполняем вращение
        A = rotate(A, p, q)
        V = V @ rotate(np.eye(n), p, q)

    values = np.diag(A)
    vectors = V

    return values, vectors


# Пример использования
A = np.array([[4, 1, 2],
              [1, 3, 0],
              [2, 0, 5]])

values, vectors = count(A)

print("Собственные значения:")
print(values)
print("Собственные векторы:")
print(vectors)