def hitung_bonus_tahunan(performa, gaji_tahunan):
    # Menghitung bonus menggunakan percabangan ternary
    bonus = (
        0.20 * gaji_tahunan if performa == 5 else
        0.10 * gaji_tahunan if performa == 4 else
        0.05 * gaji_tahunan if performa == 3 else
        0.02 * gaji_tahunan if performa == 2 else
        0  # Tidak ada bonus untuk performa 1
    )

    # Menampilkan hasil
    print(f"Performa Karyawan: {performa}")
    print(f"Gaji Tahunan: Rp {gaji_tahunan:,.2f}")
    print(f"Bonus Tahunan: Rp {bonus:,.2f}")

# Contoh penggunaan
performa_karyawan = int(input("Masukkan nilai performa karyawan (1-5): "))
gaji_tahunan_karyawan = float(input("Masukkan gaji tahunan karyawan: "))

hitung_bonus_tahunan(performa_karyawan, gaji_tahunan_karyawan)
