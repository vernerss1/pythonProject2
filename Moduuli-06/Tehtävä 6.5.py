'''
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen
kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan,
kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

'''

def muokkaa_listaa(lista_parametri):
    muokattu_lista = []
    for alkio in lista_parametri:
        if alkio > 10:
            muokattu_lista.append(alkio)
    return muokattu_lista


testi_lista = [1, 56, 23, 2, 4]
print(muokkaa_listaa(testi_lista))
print(testi_lista)
