'''
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
'''

sukup = input("Anna sukupuoli (N/M) ")
hemoglob = int (input("Anna hemoglobiinin arvo: "))
if sukup == "N":
    if hemoglob > 175:
        print("Hemoglobiinniarvosi on korkea")
    elif hemoglob < 117:
        print("Hemoglobiini on alhainen")
    elif 117<=hemoglob<175:
        print("Hemoglobiii on normaali")

if sukup == "M":
    if  hemoglob > 195:
        print("Hemoglobiinniarvosi on korkea")
    elif hemoglob < 134:
        print("Hemoglobiini on alhainen")
    elif 134<=hemoglob<195:
        print("Hemoglobiii on normaali")




