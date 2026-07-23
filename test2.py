def cek_genap_ganjil():
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan Genap")
    else:
        print(f"{angka} adalah bilangan Ganjil")

        
def konversi_suhu():
    celsius = float(input("Masukkan suhu (Celsius): "))
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    
    print(f"{celsius}°C = {fahrenheit}°F")
    print(f"{celsius}°C = {kelvin}K")


def hitung_luas_keliling_persegi():
    sisi = float(input("Masukkan panjang sisi persegi: "))
    luas = sisi * sisi
    keliling = 4 * sisi
    
    print(f"Luas persegi = {luas}")
    print(f"Keliling persegi = {keliling}")


def tampilkan_menu():
    print("\n=== MENU PENGHITUNGAN ===")
    print("1. Cek Genap/Ganjil")
    print("2. Konversi Suhu (Celsius ke Fahrenheit & Kelvin)")
    print("3. Hitung Luas & Keliling Persegi")
    print("0. Keluar")


def tanya_lanjut_atau_kembali():
    """Menanyakan apakah user mau ulangi menu yang sama (y) atau kembali ke menu utama (n).
    Return True kalau mau ulangi (y), False kalau mau kembali ke menu utama (n)."""
    while True:
        jawaban = input("\nUlangi menu ini? (y/n): ").lower()
        
        if jawaban == "y":
            return True
        elif jawaban == "n":
            return False
        else:
            print("Input tidak valid! Ketik 'y' atau 'n'.")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (0-3): ")
        
        try:
            if pilihan == "1":
                while True:
                    cek_genap_ganjil()
                    if not tanya_lanjut_atau_kembali():
                        break
            elif pilihan == "2":
                while True:
                    konversi_suhu()
                    if not tanya_lanjut_atau_kembali():
                        break
            elif pilihan == "3":
                while True:
                    hitung_luas_keliling_persegi()
                    if not tanya_lanjut_atau_kembali():
                        break
            elif pilihan == "0":
                print("Program selesai. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid! Silakan pilih 0-3.")
        except ValueError:
            print("Input tidak valid! Masukkan angka yang benar.")

            
main()