import numpy as np #library

# Mendefinisikan fungsi biseption yang akan menghitung akar dengan interval [a,b] dengan toleransi e
def bisection(f, a, b, e): 
    if np.sign(f(a)) == np.sign(f(b)): # Memeriksa tanda sign f(a) sama dengan f(b)
        raise Exception ('tidak ada akar di interval a dan b') # jika sama, berarti tidak ada akar didalamnya
    
    c = (a + b) / 2 # Menghitung titik tengah akar
    
    # Jika nilai fungsi pada titik tengah kurang dari toleransi, kembalikan titik tengah sebagai akar yang ditemukan
    if np.abs(f(c)) < e:
        return c
    # Jika tanda fungsi di a dan m sama, cari akar dalam interval [m, b]
    elif np.sign(f(a)) == np.sign(f(c)):
        return bisection(f, c, b, e)
    # Jika tanda fungsi di b dan m sama, cari akar dalam interval [a, m]
    elif np.sign(f(b)) == np.sign(f(c)):
        return bisection(f, a, c, e)

# Fungsi pertama: f(x) = x^3 - 2x + 1
f1 = lambda x: x**3 - 2*x + 1

# Mencari akar f1 dalam interval [-2, 2] dengan toleransi 0.01
r1 = bisection(f1, -2, 2, 0.01)
print("r1 =", r1)
print("f1(r1) =", f1(r1))

# Fungsi kedua: f(x) = e^x - x
f2 = lambda x: np.exp(x) - x

# Mencari akar f2 dalam interval [0, 1] dengan toleransi 0.01
r2 = bisection(f2, 0, 1, 0.01)
print("r2 =", r2)
print("f2(r2) =", f2(r2))
