'''
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
 Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
  Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
 (Oikea käyttäjätunnus on python ja salasana rules).
'''

print('Kirjoita käyttäjä ja salasana')
yritykset=0
while yritykset < 5:
    käyttäjä = input('Käyttäjänimi: ')
    salasana = input('Salasana: ')
    if salasana=='rules' and käyttäjä=='python':
        print('Tervetuloa')
        break
    else:
        print('Pääsy evätty')
        yritykset += 1