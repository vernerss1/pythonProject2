'''
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.
'''

import random
summa = 0
lukumäärä = int(input("Anna arpakuutioiden lukumäärä: "))



for kierros in range (lukumäärä):
    noppa = random.randint(1, 6)
    summa = summa + noppa
    print(f"Nopan arvo, {noppa}")

print(str(summa))




