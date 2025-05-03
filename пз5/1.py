import numpy as np

def simple_iteration(A, b, x0=None, tol=1e-10, max_iter=1000):
    n = A.shape[0]
    if x0 is None:
        x0 = np.zeros(n)
    G = np.eye(n) - np.linalg.inv(A) @ A
    d = np.linalg.inv(A) @ b

    x = x0
    for k in range(max_iter):
        x_new = G @ x + d
        # Проверка на сходимость
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"Сошлось за {k + 1} итераций.")
            return x_new
        x = x_new
    print("Не сошлось.")
    return x

A = np.array([[2, 1, 1],
              [1, 3, 2],
              [1, 2, 4]])
b = np.array([1, 2, 3])
answer = simple_iteration(A, b)
print(answer)
