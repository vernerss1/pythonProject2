'''
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
 Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
 Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
 Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma,
 jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
  Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
'''

class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        uusi_nopeus = self.nykyinen_nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nykyinen_nopeus = 0
        else:
            self.nykyinen_nopeus = uusi_nopeus

    def kulje(self):
        matka = self.nykyinen_nopeus
        self.kuljettu_matka += matka
        return self.kuljettu_matka

    def str(self):
        return f"Rekisteritunnus: {self.rekisteri}\nHuippunopeus: {self.huippunopeus}\nNykyinen nopeus: {self.nykyinen_nopeus}\nKuljettu matka: {self.kuljettu_matka}"


class Sähköauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteri, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def __str__(self):
        return super().str() + f"\nAkkukapasiteetti: {self.akkukapasiteetti}"


class Polttomoottori(Auto):
    def __init__(self, rekisteri, huippunopeus, bensatankki_koko):
        super(). __init__(rekisteri, huippunopeus)
        self.bensatankki_koko = bensatankki_koko

    def __str__(self):
        return super().str() + f"\nBensatankin koko: {self.bensatankki_koko} litraa"


sahkoauto = Sähköauto("ABC-15", 180, 52.5)
bensaauto = Polttomoottori("ACD-123", 165, 32.3)

sahkoauto.kiihdytä(50)
bensaauto.kiihdytä(40)

for i in range(3):
    sahkoauto.kulje()
    bensaauto.kulje()

print("Sähköauton matkamittarilukema:", sahkoauto.kuljettu_matka)
print("Polttomoottoriauton matkamittarilukema:", bensaauto.kuljettu_matka)

print("Sähköauton tiedot:")
print(sahkoauto)
print("")

print("Polttomoottoriauton tiedot:")
print(bensaauto)
print("")