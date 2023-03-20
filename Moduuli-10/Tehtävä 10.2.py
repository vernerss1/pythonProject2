'''
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
'''

class Hissi:
    pass

    def __init__(self, alin_kerros, ylin_kerros):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.kerros = alin_kerros

    def kerros_ylös(self):
        self.kerros = self.kerros + 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerrokesssa {self.kerros}.")
        return

    def siirry_kerrokseen(self, uusi_kerros):
        while self.kerros < uusi_kerros:
            self.kerros_ylös()
        while self.kerros > uusi_kerros:
            self.kerros_alas()
        if self.kerros == uusi_kerros:
            print(f"Olet haluamassassi kerroksessa, kerros {uusi_kerros:.0f}:ssa!")

class Talo:

    def __init__(self, alin, ylin, lkm):
        # luodaan lista talon hissejä varten
        self.hissit = []
        # luodaan uudet hissit ja lisätään ne listaan
        for nro in range(lkm):
            hissi = Hissi(alin, ylin)
            # hissit menevät nyt listassa indekseihin 1, 2, 3, ...
            self.hissit.insert(nro+1, hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero -1]
        print(f"Ajetaan hissiä {hissin_numero} kerrokseen {kohdekerros}")
        hissi.siirry_kerrokseen(kohdekerros)


talo = Talo(alin=1, ylin=7, lkm=3)
talo.aja_hissiä(1, 3)
talo.aja_hissiä(2, 7)
talo.aja_hissiä(3, 5)
