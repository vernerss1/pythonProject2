'''
Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
'''

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

auto = Auto("ABC-123", 142)
print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", auto.huippunopeus, "km/h")
print("Tämänhetkinen nopeus:", auto.nopeus, "km/h")
print("Kuljettu matka:", auto.kuljettu_matka, "km")

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Uusi nopeus: {auto.nopeus} km")

auto.kiihdytä(-200)
print(f"Hätäjarrutuksen jälkeen nopeus: {auto.nopeus} km ")

auto.kiihdytä(60)
print(f"Uusi nopeus {auto.nopeus}km")

auto.kulje(1.5)
print(f"Kuljettu matka: {auto.kuljettu_matka} km")
