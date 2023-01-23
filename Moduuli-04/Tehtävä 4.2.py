'''
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä
antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
'''
import math

tuuma = float(input("Lisää tuumamäärä: "))
print(tuuma, "tuumaa")

muutos = tuuma * 2.54

while tuuma >=1:
    print(muutos, "cm")
    tuuma = float(input("Lisää tuumamäärä: "))
    muutos = tuuma * 2.54

if tuuma <= 0:
    print("Ei voida muuntaa")