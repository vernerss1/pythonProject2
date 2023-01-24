'''
Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
Liian pieni arvaus tai Oikein. Huomaa,
että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

'''


import random
koneen_arvaus = random.randint(1, 10)
Arvaus = int(input("Anna kokonaisluku 1-10 väliltä: "))

while koneen_arvaus != Arvaus:
    if Arvaus < koneen_arvaus:
        print("Arvaa uudelleen, liian pieni arvuas!")
    elif Arvaus > koneen_arvaus:
        print("Arvaa uudelleen, arvaus liian suuri")
    Arvaus = int(input("Anna kokonaisluku 1-10 väliltä: "))
else:
    print("Oikein")