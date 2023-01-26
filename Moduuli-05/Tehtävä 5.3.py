'''
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
'''

lista = []
total = 0
luku = int(input("Anna luku: "))

for n in range(1, luku):
    if luku % n== 0:
        total = total +1

if total <= 1:
    print(f"Luku {luku} on alkuluku")
else: print(f"Luku {luku} ei ole alkuluku")
