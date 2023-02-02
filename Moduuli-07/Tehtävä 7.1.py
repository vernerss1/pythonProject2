'''
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

'''

# Määritellään monikkorakenne
vuodenajat = ("kevät", "kesä", "syksy", "talvi")

# Kysytään käyttäjältä kuukauden numero (1-12)
kkNro = int(input("Anna kuukauden numero (1-12): "))

# Määritellään, mihin vuodenaikaan kuukausi kuuluu

# Hyödynnetään monikkoa
if(kkNro == 1 or kkNro == 2 or kkNro == 12):
    vuodenaika = vuodenajat[3]
elif(kkNro >= 3 and kkNro <= 5):
    vuodenaika = vuodenajat[0]
elif(kkNro >= 6 and kkNro <= 8):
    vuodenaika = vuodenajat[1]
elif(kkNro >= 9 and kkNro <= 11):
    vuodenaika = vuodenajat[2]
else:
    vuodenaika = "tuntematon"
# Tulostetaan vastaus
print(f"{kkNro}. kuukausi kuuluu vuodenaikaan: {vuodenaika}")