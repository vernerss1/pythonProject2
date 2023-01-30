'''
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina
per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat
sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle
(eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on
hyödynnettävä kirjoitettua funktiota.
'''
#funktion lauseke
def pizzan_arvo(pizza,price):
    import math

    m2 = pizza/1000 * math.pi
    worth = price/m2
    return worth

pizza1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
pizza12 = float(input("Anna ensimmäisen pizzan hinta: "))
pizza2 = float(input("Anna  toisen pizzan halkaisija: "))
pizza22= float(input("Anna toisen pizzan hinta: "))

pizza1 = pizzan_arvo(pizza1,pizza12)
print(pizza1,"€/m2")

pizza2 = pizzan_arvo(pizza2, pizza22)
print(pizza2,"€/m2")

# Parempi vastike
if pizza1 < pizza2:
    print(pizza1,'€/m2', "pizza1 antaa paremman vastikkeen")
elif pizza2 < pizza1:
    print(pizza2,"€/m2",  'pizza2 antaa paremman vastikkeen')

