'''
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
hakea jo syötetyn lentoaseman tiedot vai lopettaa.
Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)
'''
lentoasemat = {}
def lisaa():
    print("Kohta valmis!")
    tunnus = input("Anna lentoaseman tunnus: ")
    nimi = input("Anna lentoaseman nimi: ")
    lentoasemat[tunnus] = nimi
    return

def hae():
    koodi = input("Anna ICAO-koodi")
    if koodi in lentoasemat:
        print(lentoasemat[koodi])


    print("Kyllä tämäkin valmistuu...")
    return

def tulosta():
    for asema in lentoasemat:
        print(f"{asema}")
    return

lentoasemat = {"Helsinki-Vantaa lentoasema" : "EFHK"}

toiminto = -1

while toiminto !=3:
    print("0 = tulosta lentoasemien tiedot")
    print("1 = lisää uusi lentoasema: ")
    print("2 = hae lentoasema")
    print("3 = lopeta")

    toiminto = int(input("Valitse toiminto: "))
    if toiminto == 0:
        tulosta()
    elif toiminto == 1:
        lisaa()
    elif toiminto == 2:
        hae()



print("Kiitos ja näkemiin")
