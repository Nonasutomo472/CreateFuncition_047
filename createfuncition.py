def konversi_suhu(nilai, satuan):
    # Mengecek apakah satuan yang diberikan adalah 'C' (Celsius)
    if satuan == 'C':
        # Jika satuan adalah Celsius, maka konversi ke Fahrenheit
        return (nilai * 9/5) + 32
    # Mengecek apakah satuan yang diberikan adalah 'F' (Fahrenheit)
    elif satuan == 'F':
        # Jika satuan adalah Fahrenheit, maka konversi ke Celsius
        return (nilai - 32) * 5/9
    else:
        # Jika satuan tidak valid, tampilkan pesan error
        return "Satuan tidak valid! Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."

# Contoh penggunaan fungsi untuk konversi dari Celsius ke Fahrenheit
nilai_celsius = 25
konversi_ke_fahrenheit = konversi_suhu(nilai_celsius, 'C')
print(f"{nilai_celsius}°C adalah {konversi_ke_fahrenheit}°F")

# Contoh penggunaan fungsi untuk konversi dari Fahrenheit ke Celsius
nilai_fahrenheit = 77
konversi_ke_celsius = konversi_suhu(nilai_fahrenheit, 'F')
print(f"{nilai_fahrenheit}°F adalah {konversi_ke_celsius}°C")

import math

# Fungsi lambda untuk menghitung luas lingkaran berdasarkan rumus: π * r^2
# Input: jari-jari lingkaran
# Output: luas lingkaran
luas_lingkaran = lambda jari_jari: math.pi * jari_jari**2

# Contoh penggunaan fungsi lambda untuk menghitung luas lingkaran
jari_jari = 5
luas = luas_lingkaran(jari_jari)

# Menampilkan hasil perhitungan luas lingkaran
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")
