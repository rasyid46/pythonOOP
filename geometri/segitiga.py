from geometri.bangun_ruang import BangunRuang


class Segitiga(BangunRuang):
    def __init__(self, a, t):
        # fungsi yang dipanggil pertama kali
        self.a = a
        self.t = t

    @property
    def info(self):
        return f'ini objek menghitung luas Segiga Alas {self.a} tinggi {self.t}'

    def hitung_luas(self):
        return self.a * self.t / 2
