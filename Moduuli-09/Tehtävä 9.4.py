'''
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

'''

import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeus_muutos):
        uusi_nopeus = self.nopeus + nopeus_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tunti_maara):
        matka = self.nopeus * tunti_maara
        self.kuljettu_matka += matka


autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailun_kesto = 0
voittaja = None


while voittaja is None:
    kilpailun_kesto += 1
    for auto in autot:
        nopeus_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeus_muutos)
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            voittaja = auto
            break


for auto in autot:
    print("Rekisteritunnus:", auto.rekisteritunnus)
    print("Huippunopeus:", auto.huippunopeus, "km/h")
    print("Kuljettu matka:", auto.kuljettu_matka, "km")
    if auto == voittaja:
        print("VOITTAJA!")
    print("--------------------")