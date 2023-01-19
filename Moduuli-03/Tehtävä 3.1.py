'''
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
 Jos kuha on alamittainen,
  ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
 montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
  Kuha on alamittainen, jos sen pituus on alle 37 cm.
'''

kuha = int(input("Anna kuhan pituus senttimetreinä: "))
if  (kuha < 37):
    print("Laske kuha järveen", 37 - kuha,)

else: print("Kuha on", kuha, "cm")