# Daftar rokok dan harga
daftar_rokok = {
    "WinBold": 26000,
    "Juara Filter": 22000,
    "Gudang Berkah": 15000,
    "Surya Pro": 20000,
    "Magnum Filter": 25000
    
}

# Menampilkan daftar rokok yang tersedia
print("Daftar Rokok yang Tersedia:")
for rokok, harga in daftar_rokok.items():
    print(f"{rokok}: Rp {harga:,.0f}")

# Inisialisasi variabel total harga
total_harga = 0

# Input dari pengguna untuk memilih rokok
#looping while
while True:
    pilihan = input("Pilih rokok yang ingin dibeli (Ketik 'selesai' untuk mengakhiri pembelian): ")
    
    if pilihan.lower() == "selesai":
        break

    if pilihan in daftar_rokok:
        harga_rokok = daftar_rokok[pilihan]
        total_harga += harga_rokok
        print(f"{pilihan} ditambahkan ke keranjang belanja.")
    else:
        print("Rokok tidak valid. Silakan pilih rokok yang tersedia.")

# Menampilkan total harga
print(f"Total harga pembelian: Rp {total_harga:,.0f}")

# Terima kasih
print("Terima kasih telah berbelanja!")