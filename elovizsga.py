from abc import ABC


class Szoba(ABC):
    pass
    def __init__(self, ar, szobaszam):
        self.ar=ar
        self.szobaszam = szobaszam


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, reggeliara):
        super().__init__(ar=50, szobaszam=szobaszam)
        self.reggeliara = reggeliara


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, wifiara):
        super().__init__(ar=100, szobaszam=szobaszam)
        self.wifiara = wifiara


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum


print('vege')