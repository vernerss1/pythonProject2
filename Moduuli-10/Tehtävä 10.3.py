'''
Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
'''

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.kerros = alin_kerros

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

    def siirry_kerrokseen(self, uusi_kerros):
        while self.kerros < uusi_kerros:
            self.kerros_ylös()
        while self.kerros > uusi_kerros:
            self.kerros_alas()
        if self.kerros == uusi_kerros:
            print(f"Olet haluamassasi kerroksessa, kerros {uusi_kerros:.0f}:ssa!")

class Talo:
    def __init__(self, alin, ylin, lkm):
        self.hissit = []
        for nro in range(lkm):
            hissi = Hissi(alin, ylin)
            self.hissit.append(hissi)
        self.alin_kerros = alin

    def aja_hissiä(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero - 1]
        print(f"Ajetaan hissiä {hissin_numero} kerrokseen {kohdekerros}")
        hissi.siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        print("Kaikki hissit kutsutaan pohjakerrokseen.")
        for hissi in self.hissit:
            print(f"Ajetaan hissiä {self.hissit.index(hissi) + 1}")
            hissi.siirry_kerrokseen(self.alin_kerros)


talo = Talo(alin=1, ylin=7, lkm=3)
talo.aja_hissiä(1, 3)
talo.aja_hissiä(2, 7)
talo.aja_hissiä(3, 5)
print("Palohälytys")
talo.palohälytys()

