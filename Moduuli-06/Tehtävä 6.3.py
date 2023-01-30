'''
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.

'''
def muunnos(gallona):
    litra = gallona * 3.785
    return litra


user_input = 0
while user_input >= 0:
    user_input = float(input("Anna galloona määrä: "))
    if user_input > 0:
        result = muunnos(user_input)
        print(result, "litraa")
print("Ohjelma sammutetaan")


