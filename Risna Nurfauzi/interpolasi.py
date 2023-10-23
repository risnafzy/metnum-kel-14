import matplotlib.pyplot as plt
import numpy as np

# Data titik-titik yang diketahui
x = [0, 20, 40, 60, 80, 100]
y = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]

m = len(x)
n = m - 1  # Derajat polinom interpolasi

xp = 20  # Nilai yang ingin diinterpolasi

# Membuat array xplt untuk plotting hasil interpolasi
xplt = np.linspace(x[0], x[-1], num=100)
yplt = []

# Melakukan interpolasi menggunakan Metode Lagrange pada semua titik xplt
for i in range(len(xplt)):
    yp = 0
    for j in range(n + 1):
        p = 1
        for k in range(n + 1):
            if k != j:
                p *= (xplt[i] - x[k]) / (x[j] - x[k])
        yp += y[j] * p
    yplt.append(yp)

print("xplt:", xplt)
print("yplt:", yplt)

# Menghitung nilai interpolasi pada titik xp
yp = 0  # Inisialisasi yp
for i in range(n + 1):
    p = 1
    for j in range(n + 1):
        if j != i:
            p *= (xp - x[j]) / (x[i] - x[j])
    yp += y[i] * p

print("Untuk x = %.2f maka y = %.2f" % (xp, yp))

# Menampilkan grafik titik-titik data, hasil interpolasi, dan nilai interpolasi pada x=20
plt.plot(x, y, 'bo', label='Data')
plt.plot(xplt, yplt, 'r-', label='Interpolasi')
plt.scatter(xp, yp, color='green', marker='o', label='Interpolasi pada x=20')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolasi Metode Lagrange')
plt.grid(True)
plt.show()
