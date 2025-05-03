import numpy as np

def seidel(A, b, x0=None, tol=1e-10, max_iterations=100):
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)  # Начальное приближение

    x = x0.copy()

    for iteration in range(max_iterations):
        x_old = x.copy()

        for i in range(n):
            # Вычисляем i-ю компоненту вектора x
            sum_ax = np.dot(A[i], x) - A[i, i] * x[i]
            x[i] = (b[i] - sum_ax) / A[i, i]

        # Проверяем на сходимость
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            print(f"Сошлось за {iteration + 1} итераций.")
            return x

    print("Не сошлось за максимальное количество итераций.")
    return x

# Пример использования
A = np.array([
    [10, 1, 1],
    [2, 10, 1],
    [2, 2, 10]],
    dtype=float)
b = np.array([12, 13, 14], dtype=float)

solution = seidel(A, b)
print("Решение:", solution)
