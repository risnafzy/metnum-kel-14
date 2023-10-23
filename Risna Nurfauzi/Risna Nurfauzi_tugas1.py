# Import library numpy dengan alias np
import numpy as np

# Mendefinisikan fungsi my_bisection yang akan menghitung akar suatu fungsi f dalam interval [a, b] dengan toleransi e
def my_bisection(f, a, b, e):
    # Memeriksa apakah tanda (sign) dari f(a) sama dengan tanda f(b).
    # Jika sama, maka tidak mungkin terdapat akar di dalam interval [a, b].
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    
    # Menghitung titik tengah m dari interval [a, b]
    m = (a + b) / 2
    
    # Jika nilai mutlak dari f(m) lebih kecil dari toleransi e, maka akar telah ditemukan.
    if np.abs(f(m)) < e:
        return m
    # Jika tanda f(a) sama dengan tanda f(m), maka akar berada di interval [m, b].
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, e)
    # Jika tanda f(b) sama dengan tanda f(m), maka akar berada di interval [a, m].
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, e)

# Fungsi pertama: f(x) = x^3 - 2x + 1
f1 = lambda x: x**3 - 2*x + 1

# Menggunakan metode bisection untuk mencari akar f1 dalam interval [-2, 2] dengan toleransi 0.01
r1 = my_bisection(f1, -2, 2, 0.01)
print("r1 =", r1)
print("f1(r1) =", f1(r1))

# Fungsi kedua: f(x) = e^x - x
f2 = lambda x: np.exp(x) - x

# Menggunakan metode bisection untuk mencari akar f2 dalam interval [0, 1] dengan toleransi 0.01
r2 = my_bisection(f2, 0, 1, 0.01)
print("r2 =", r2)
print("f2(r2) =", f2(r2))