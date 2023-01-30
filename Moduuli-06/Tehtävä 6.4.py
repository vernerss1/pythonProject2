'''
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan,
kutsut funktiota ja tulostat sen palauttaman summan.
'''


def summa(lista_parametri):
    total = 0
    for n in lista_parametri:
        total += n
    return total

lista_parametri = [1, 2, 3, 4, 5]
print(summa(lista_parametri))


