import numpy as np

def LU_decomposition(A, n):
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1

    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]
        for j in range(i+1, n):
            L[j][i] = A[j][i]
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] /= U[i][i]

    return L, U

def forward_substitution(L, b, n):
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
    return y

def backward_substitution(U, y, n):
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x

# Contoh input matriks A dan vektor b
A = np.array([[2, -1, 1],
              [1, 3, 2],
              [1, 1, 3]])

b = np.array([8, 10, 12])

n = len(b)

# Mendekomposisi matriks A menjadi L dan U
L, U = LU_decomposition(A, n)

# Menyelesaikan sistem persamaan menggunakan metode LU
y = forward_substitution(L, b, n)
x = backward_substitution(U, y, n)

print("Matriks L:")
print(L)
print("Matriks U:")
print(U)
print("Vektor y:")
print(y)
print("Vektor x (solusi sistem persamaan):")
print(x)
