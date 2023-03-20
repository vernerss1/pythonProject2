'''
Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen,
kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.
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

eka_hissi = Hissi(0,7)
eka_hissi.siirry_kerrokseen(5)
eka_hissi.siirry_kerrokseen(1)
