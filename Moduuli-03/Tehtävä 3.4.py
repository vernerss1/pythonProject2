'''
Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
Vuosi on karkausvuosi, jos se on jaollinen neljällä.
Sadalla jaolliset vuodet ovat karkausvuosia vain
jos ne ovat jaollisia myös neljälläsadalla.
'''

'''
Testi:
2000: On 
1900: Ei ole
2023: Ei ole
2024: On 
'''

karkausvuosi = int(input("Lisää vuosiluku: "))
if (karkausvuosi % 4 == 0 ) and (karkausvuosi % 100 != 0) or (karkausvuosi % 400 == 0):
    print("Se on karkausvuosi")
else:
    print("Ei ole")

