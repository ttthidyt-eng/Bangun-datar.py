import math

def hitung_persegi():
    while True:
        print("\n--- Persegi ---")
        sisi = float(input("Masukkan panjang sisi: "))
        luas = sisi * sisi
        keliling = 4 * sisi
        print(f"Luas Persegi: {luas}")
        print(f"Keliling Persegi: {keliling}")

        ulang = input("Hitung persegi lagi? (y/n): ").lower()
        if ulang != "y":
            break

def hitung_persegi_panjang():
    while True:
        print("\n--- Persegi Panjang ---")
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        print(f"Luas Persegi Panjang: {luas}")
        print(f"Keliling Persegi Panjang: {keliling}")

        ulang = input("Hitung persegi panjang lagi? (y/n): ").lower()
        if ulang != "y":
            break

def hitung_lingkaran():
    while True:
        print("\n--- Lingkaran ---")
        radius = float(input("Masukkan jari-jari: "))
        luas = math.pi * radius**2
        keliling = 2 * math.pi * radius
        print(f"Luas Lingkaran: {luas:.2f}")
        print(f"Keliling Lingkaran: {keliling:.2f}")

        ulang = input("Hitung lingkaran lagi? (y/n): ").lower()
        if ulang != "y":
            break

def hitung_segitiga():
    while True:
        print("\n--- Segitiga (Siku-siku) ---")
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = 0.5 * alas * tinggi
        sisi_miring = math.sqrt(alas**2 + tinggi**2)
        keliling = alas + tinggi + sisi_miring
        print(f"Luas Segitiga: {luas}")
        print(f"Keliling Segitiga: {keliling:.2f}")

        ulang = input("Hitung segitiga lagi? (y/n): ").lower()
        if ulang != "y":
            break

def main():
    while True:
        print("\n=== Program Hitung Bangun Datar ===")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Lingkaran")
        print("4. Segitiga")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            hitung_persegi()
        elif pilihan == '2':
            hitung_persegi_panjang()
        elif pilihan == '3':
            hitung_lingkaran()
        elif pilihan == '4':
            hitung_segitiga()
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()