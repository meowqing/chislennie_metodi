import numpy as np


def power_iteration(A, num_iterations: int):
    b_k = np.random.rand(A.shape[1])

    for _ in range(num_iterations):
        b_k1 = np.dot(A, b_k)

        b_k1_norm = np.linalg.norm(b_k1)
        b_k = b_k1 / b_k1_norm

    # Собственное значение
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k)) / np.dot(b_k.T, b_k)
    return eigenvalue, b_k


# Пример использования
A = np.array([[4, 1],
                  [2, 3]])
num_iterations = 100
eigenvalue, eigenvector = power_iteration(A, num_iterations)

print("Наибольшее собственное значение:", eigenvalue)
print("Собственный вектор:", eigenvector)
