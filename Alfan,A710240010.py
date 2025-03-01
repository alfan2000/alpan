class Komputer:
    def __init__(self, merek, ram, prosesor, vga):
        self.merek = merek
        self.ram = ram
        self.prosesor = prosesor
        self.vga = vga

    def hidupkan(self):
        print(f"Komputer {self.merek} dihidupkan.")

    def matikan(self):
        print(f"Komputer {self.merek} dimatikan.")

    def buka_aplikasi(self, aplikasi):
        print(f"Membuka aplikasi {aplikasi} di komputer {self.merek}.")

    def tutup_aplikasi(self, aplikasi):
        print(f"Menutup aplikasi {aplikasi} di komputer {self.merek}.")

komputer1 = Komputer(merek="MSI", ram="16GB", prosesor="Ryzen 5", vga="AMD RX 6650M")
komputer2 = Komputer(merek="LENOVO", ram="16GB", prosesor="Intel i5", vga="RTX 3050 ")

print(f"Merek: {komputer1.merek}")
print(f"RAM: {komputer1.ram}")
print(f"Prosesor: {komputer1.prosesor}")
print(f"VGA: {komputer1.vga}")

komputer1.hidupkan()
komputer1.matikan()
komputer1.buka_aplikasi(aplikasi="Chrome")
komputer1.tutup_aplikasi(aplikasi="Chrome")

print(f"Merek: {komputer2.merek}")
print(f"RAM: {komputer2.ram}")
print(f"Prosesor: {komputer2.prosesor}")
print(f"VGA: {komputer2.vga}")

komputer2.hidupkan()
komputer2.matikan()
komputer2.buka_aplikasi(aplikasi="VS Code")
komputer2.tutup_aplikasi(aplikasi="VS Code")
