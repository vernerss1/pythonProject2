
#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

korkeus_input = input("Suorakulmion korkeus:")
kanta_input = input("Suorakulmion kanta:")

kanta = float(kanta_input)
korkeus = float(korkeus_input)

#Laske pinta-ala
print("Suorakulmion pinta-ala", kanta * korkeus)
print(("Suorakulmion piiri"), kanta + korkeus + kanta + korkeus)