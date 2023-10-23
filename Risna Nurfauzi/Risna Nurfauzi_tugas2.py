import numpy as np
import matplotlib.pyplot as plt

def my_bisection(f, a, b, e, max_iter):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar di interval a dan b')

    m_values = []  # List untuk menyimpan nilai tengah m pada setiap iterasi
    
    for i in range(max_iter):
        m = (a + b) / 2
        m_values.append(m)  # Menambahkan nilai tengah ke dalam list
        
        if np.abs(f(m)) < e:
            return m, m_values
        elif np.sign(f(a)) == np.sign(f(m)):
            a = m
        elif np.sign(f(b)) == np.sign(f(m)):
            b = m

    raise Exception(f'Akar tidak ditemukan dalam {max_iter} iterasi')

# Input fungsi dari pengguna
expression = input("Masukkan fungsi (gunakan x sebagai variabel): ")
f = lambda x: eval(expression)

# Input batas a, b, galat e, dan iterasi ke-n dari pengguna
a = float(input("Masukkan batas a: "))
b = float(input("Masukkan batas b: "))
e = float(input("Masukkan galat e: "))
n = int(input("Masukkan iterasi ke-n: "))

try:
    r, m_values = my_bisection(f, a, b, e, n)
    print("Akar yang ditemukan:", r)

    # Menampilkan grafik fungsi
    x_values = np.linspace(a, b, 100)
    y_values = [f(x) for x in x_values]

    plt.plot(x_values, y_values, label='f(x)')
    plt.scatter(m_values, [f(x) for x in m_values], color='red', marker='x', label='Iterasi')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Grafik fungsi {expression}')
    plt.legend()
    plt.grid(True)
    plt.show()

except Exception as e:
    print(e)