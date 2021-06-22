from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self,p,l):
        #fungsi yang dipanggil pertama kali
        self.p = p
        self.l =l

    @property
    def info(self):
        return f'ini objek menghitung luas Persegi panjang dengan Panjang {self.p} lebar {self.l}'

    def hitung_luas(self):
        return self.p*self.l
