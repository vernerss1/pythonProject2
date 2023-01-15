#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

x = int(input("lisää numero 1:"))
y = int(input("lisää numero 2:"))
z = int(input("lisää numero 3:"))

print("Numerot ovat", x,y,z)

summa = x + y + z

tulo = x * y * z

keskiarvo = (x + y + z) / 3

print("lukujen summa", summa)
print("lukujen tulo", tulo)
print("lukujen keskiarvo", keskiarvo)


