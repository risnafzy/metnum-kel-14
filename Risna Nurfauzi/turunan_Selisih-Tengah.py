import numpy as np  # library

def hitung_turunan_selisih_tengah(data, h):
    turunan = []

    for i in range(len(data) - 1):  
        f_x_plus_h = data[i + 1]
        f_x_minus_h = data[i - 1] if i > 0 else data[i]  
        turunan_h = (f_x_plus_h - f_x_minus_h) / (2 * h)
        turunan.append(turunan_h)

    return turunan

def main():
    # Input data dari pengguna
    data_input = input("Masukkan data yang dipisahkan oleh spasi: ")
    data = [float(x) for x in data_input.split()]

    # Input nilai h dari pengguna
    h = float(input("Masukkan nilai h: "))

    # Hitung turunan selisih tengah
    turunan_selisih_tengah = hitung_turunan_selisih_tengah(data, h)

    # Tampilkan hasil
    print("Hasil Turunan Selisih Tengah:")
    for i, turunan in enumerate(turunan_selisih_tengah):
        print(f"f'({data[i+1]}) = {turunan}")

if __name__ == "__main__":
    main()