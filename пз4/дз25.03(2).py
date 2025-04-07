import numpy as np

def gauss_elimination_with_partial_pivoting(A, b):
    n = len(b)

    # Прямой ход с выбором ведущего элемента
    for i in range(n):
        # Поиск максимального элемента в текущем столбце
        max_row_index = np.argmax(np.abs(A[i:n, i])) + i
        # Обмен строк, если необходимо
        if max_row_index != i:
            A[[i, max_row_index]] = A[[max_row_index, i]]
            b[i], b[max_row_index] = b[max_row_index], b[i]

        # Приведение к верхнетреугольному виду
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            A[j] = A[j] - factor * A[i]
            b[j] -= factor * b[i]

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i][i]

    return x

A = np.array([[3, 2, -4],
                  [2, 3, 3],
                  [5, -3, 1]])
b = np.array([3, 15, 14], dtype=float)
answer = gauss_elimination_with_partial_pivoting(A, b)
print("Решение системы уравнений:", answer)
