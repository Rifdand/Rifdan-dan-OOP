# class>motor
# object> surat2, kondisi_mesin, merk, model, harga, cc, warna
# nama : Rifdan (24241107)

class SepedaMotor:
    def __init__(self, surat2, kondisi_mesin, merk, model, harga, cc, warna):
        self.surat2 = surat2
        self.kondisi_mesin = kondisi_mesin
        self.merk = merk
        self.model = model
        self.harga = harga
        self.cc = cc
        self.warna = warna

    def tampilkan_info(self):
        print("===== DATA SEPEDA MOTOR =====")
        print(f"Merk            : {self.merk}")
        print(f"Model           : {self.model}")
        print(f"Warna           : {self.warna}")
        print(f"Kapasitas Mesin : {self.cc} cc")
        print(f"Harga           : Rp{self.harga:,}")
        print(f"Kondisi Mesin   : {self.kondisi_mesin}")
        print(f"Surat-surat     : {self.surat2}")
        print("=============================\n")


# contoh pemakaian
motor1 = SepedaMotor(
    surat2="Lengkap (STNK & BPKB)",
    kondisi_mesin="Baik",
    merk="Honda",
    model="Beat",
    harga=18000000,
    cc=110,
    warna="Hitam"
)

motor2 = SepedaMotor(
    surat2="Lengkap",
    kondisi_mesin="Sangat Baik",
    merk="Yamaha",
    model="NMAX",
    harga=29000000,
    cc=155,
    warna="Putih"
)

motor1.tampilkan_info()
motor2.tampilkan_info()
