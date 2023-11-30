from abc import ABC, abstractclassmethod


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
        self.foglalasok = []

        def add_szoba(self, szoba):
            self.szobak.append(szoba)

        def add_foglalas(self, foglalas):
            self.foglalasok.append(foglalas)

        def foglalas(self, szobaszam, datum):
            for szoba in self.szobak:
                if szoba.szobaszam == szobaszam:
                    foglalas = Foglalas(szoba=szoba, datum=datum)
                    self.add_foglalas(foglalas)
                    return szoba.ar
            return None

        def lemondas(self, szobaszam, datum):
            for foglalas in self.foglalasok:
                if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                    self.foglalasok.remove(foglalas)
                    return "lemondva"
                return "nincs ilyen foglalas"

        def osszes_foglalas(self):
            print(f"a(z){self.nev} összes foglalása:")
            for foglalas in self.foglalasok:
                print(f"Foglalás - Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum


def menu():
    print("Válassz műveletet az alábbi lehetőségek közül:")
    print("0 - Kilépés")
    print("1 - Foglalás")
    print("2 - Lemondás")
    print("3 - Foglalások listázása")

my_szalloda = Szalloda("Bence's Hotel")
egyik_egyagyas_szoba = EgyagyasSzoba(11,1000)
masik_egyagyas_szoba = EgyagyasSzoba(12,1000)
ketagyas_szoba = KetagyasSzoba(21,500)
menu()
valasztas = input()
while True:
    if valasztas == "0":
        break
    menu()
    valasztas = input()
    if valasztas == "1":
        sorszam = input("szobaszám a szobához:")
        datum = input("dátum a foglaláshoz 2023-11-30 formátumban")
        foglalas = Foglalas(sorszam, datum)


print("Tóth Bence Dániel, RU1BB4, mérnökinformatikus BSc.")