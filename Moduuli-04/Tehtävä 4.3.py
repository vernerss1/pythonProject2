'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
'''


numero = int(input("Anna luku: "))

iso_numero = int(numero)
pieni_numero = int(numero)

while numero != "":
    numero = (input("Anna luku: "))
    if numero != "":
        numero = int(numero)
        if numero > iso_numero:
            iso_numero = numero
        elif numero < pieni_numero:
            pieni_numero = numero

print(f"Pienin {pieni_numero}, suurin antamasi {iso_numero}")


