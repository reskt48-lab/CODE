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


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (0-3): ")
        
        try:
            if pilihan == "1":
                cek_genap_ganjil()
            elif pilihan == "2":
                konversi_suhu()
            elif pilihan == "3":
                hitung_luas_keliling_persegi()
            elif pilihan == "0":
                print("Program selesai. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid! Silakan pilih 0-3.")
        except ValueError:
            print("Input tidak valid! Masukkan angka yang benar.")

            
main()