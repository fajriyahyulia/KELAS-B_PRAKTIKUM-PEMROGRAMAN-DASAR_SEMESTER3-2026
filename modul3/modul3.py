koleksi_lagu = []

def tambah_lagu(judul, penyanyi):
    lagu = {"judul": judul, "penyanyi": penyanyi}
    koleksi_lagu.append(lagu)
    print(f"Lagu '{judul}' oleh {penyanyi} berhasil ditambahkan.")

def tampilkan_lagu():
    if len(koleksi_lagu) == 0:
        print("Belum ada lagu dalam koleksi.")
    else:
        print("Daftar Koleksi Lagu:")
        for i, lagu in enumerate(koleksi_lagu, start=1):
            print(f"{i}. {lagu['judul']} - {lagu['penyanyi']}")

def hapus_lagu(judul):
    for lagu in koleksi_lagu:
        if lagu["judul"].lower() == judul.lower():
            koleksi_lagu.remove(lagu)
            print(f"Lagu '{judul}' berhasil dihapus.")
            return
    print(f"Lagu '{judul}' tidak ditemukan.")

def cari_lagu(nama_penyanyi):
    hasil = [lagu for lagu in koleksi_lagu if lagu["penyanyi"].lower() == nama_penyanyi.lower()]
    if len(hasil) == 0:
        print(f"Tidak ada lagu dari penyanyi '{nama_penyanyi}'.")
    else:
        print(f"Lagu oleh {nama_penyanyi}:")
        for lagu in hasil:
            print(f"- {lagu['judul']}")

# Pengujian program
tambah_lagu("Bohemian Rhapsody", "Queen")
tambah_lagu("Shape of You", "Ed Sheeran")
tambah_lagu("Perfect", "Ed Sheeran")

tampilkan_lagu()

print()
cari_lagu("Ed Sheeran")

print()
hapus_lagu("Shape of You")
tampilkan_lagu()
