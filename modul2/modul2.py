class Dosen:
    def __init__(self, nama, nidn, mata_kuliah):
        self.nama = nama
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah
    def update_mata_kuliah(self, mk_baru):
        self.mata_kuliah = mk_baru
        print(f"Sukses! Mata kuliah {self.nama} telah diubah menjadi: {self.mata_kuliah}")
    def info(self):
        print(f"Dosen {self.nama}, dengan NIDN {self.nidn}, mengajar mata kuliah {self.mata_kuliah}")

dosen1 = Dosen("Vearen Dika Sofirudin, S.Pd., M.Ed.", "5940777678230142", "Praktikum Pemrograman")
dosen2 = Dosen("Slamet Kurniawan Fahrurozi, S.Pd., M.Pd.", "0623109501","Keamanan Jaringan")
dosen3 = Dosen("Yusfia Hafid Aristyagama, S.T., M.T.", "0024059107", "Pengembangan Aset 2D")

dosen1.info()
dosen2.info()
dosen3.info()

dosen3.update_mata_kuliah("Praktikum Pengembangan Aset 2D")
dosen3.info()

