'''
Kirjoita while-toistorakennetta käyttävä ohjelma,
joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
'''


number = 1

while number<1000:
    if number%3==0:
        print(number)
    number = number +1