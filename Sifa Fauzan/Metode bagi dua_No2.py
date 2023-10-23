#library
import numpy as np
import matplotlib.pyplot as plt

# Definisikan fungsi bisection untuk mencari akar
def my_bisection(f, a, b, e, max_iter):
    # Periksa apakah tanda fungsi di a dan b sama.
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar di interval a dan b')  # Jika sama, maka tidak ada akar dalam interval ini.

    m_values = []  # List untuk menyimpan nilai tengah m pada setiap iterasi

    # Lakukan iterasi maksimum sebanyak iterasi maksimal
    for i in range(max_iter):
        m = (a + b) / 2  # Hitung nilai tengah m
        m_values.append(m)  # Menambahkan nilai tengah ke dalam list

        # Jika nilai dari f(m) kurang dari galat yang diinginkan (e), kembalikan hasilnya
        if np.abs(f(m)) < e:
            return m, m_values
        # Jika tanda fungsi di a dan m sama, perbarui batas b dengan m
        elif np.sign(f(a)) == np.sign(f(m)):
            a = m
        # Jika tanda fungsi di b dan m sama, perbarui batas a dengan m
        elif np.sign(f(b)) == np.sign(f(m)):
            b = m

    # Jika mencapai batas maksimum iterasi tanpa menemukan akar, akar tidak ditemukan
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
    # Panggil fungsi my_bisection untuk mencari akar
    r, m_values = my_bisection(f, a, b, e, n)
    print("Akar yang ditemukan:", r)

    # Menampilkan grafik fungsi
    x_values = np.linspace(a, b, 100)
    y_values = [f(x) for x in x_values]

    # Plot grafik fungsi dan titik-titik iterasi
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
