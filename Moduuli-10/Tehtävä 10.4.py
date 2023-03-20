'''
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen,
kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli
arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
Muussa tapauksessa palautetaan False.
Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla
kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.
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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeus_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeus_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("{:<15} {:<15} {:<15} {:<15}".format("Rekisteritunnus", "Huippunopeus", "Kuljettu matka", "Tila"))
        for auto in self.autot:
            tila = "" if auto.kuljettu_matka < self.pituus else "Maalissa"
            print("{:<15} {:<15} {:<15} {:<15}".format(auto.rekisteritunnus, auto.huippunopeus, auto.kuljettu_matka, tila))
        print("--------------------")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    tunti += 1
    kilpailu.tunti_kuluu()
    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()
