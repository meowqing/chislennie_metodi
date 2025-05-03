import numpy as np

def gram_schmidt(A):
    """метод Грамма-Шмидта для QR-разложения."""
    n, m = A.shape
    Q = np.zeros((n, m))
    R = np.zeros((m, m))

    for j in range(m):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        if R[j, j] > 0:
            Q[:, j] = v / R[j, j]

    return Q, R

def qr_algorithm(A, max_iterations=1000, tolerance=1e-10):
    n = A.shape[0]
    A_k = A.copy()
    Q_total = np.eye(n)

    for _ in range(max_iterations):
        Q, R = gram_schmidt(A_k)
        A_k = R @ Q
        Q_total = Q_total @ Q

        # Проверка на сходимость
        off_diagonal = np.sum(np.abs(A_k - np.diag(np.diag(A_k))))
        if off_diagonal < tolerance:
            break

    eigenvalues = np.diag(A_k)
    eigenvectors = Q_total

    return eigenvalues, eigenvectors

# Пример использования
A = np.array([[4, 1], [2, 3]])
eigenvalues, eigenvectors = qr_algorithm(A)

print("Собственные значения:", eigenvalues)
print("Собственные векторы:", eigenvectors)