'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi
kääntää antamalla sort-metodille argumentiksi reverse=True.

'''
lista = []
luku = input("Anna luku: ")

while luku !="":
    lista.append(int(luku))
    luku = input("Anna luku: ")
lista.sort(reverse = True)
print(lista[0:5])