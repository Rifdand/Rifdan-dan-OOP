# Rifdan - 24241107
class Kendaraan:
    pemilik = "Rifdan"

    def __init__(self, jenis, merk, tahun):
        self.jenis = jenis
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"Jenis: {self.jenis}, Merk: {self.merk}, Tahun: {self.tahun}"


mobil = Kendaraan("Mobil", "Toyota", 2020)
print(mobil.info())

motor = Kendaraan("Motor", "Honda", 2019)
print(motor.info())

print(f"Pemilik Kendaraan: {Kendaraan.pemilik}")
