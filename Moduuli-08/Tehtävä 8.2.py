'''
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa
kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta,
helikopterikenttiä on 15 kappaletta jne.

'''

import mysql.connector

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,    #Tietyille asioille on omat porttinsa esim. näppäimistö, internet
        database='flight_game',
        user='juuret',
        password='nine45',
        autocommit=True           # muutokset tietokantaan tehdään heti
        )

def lentokenttä_tyypit(maakoodi):
    large_airport = 0
    medium_airport = 0
    small_airport = 0
    closed = 0
    heliport = 0

    sql = "SELECT airport.type FROM airport WHERE airport.iso_country ='"+ maakoodi +"'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            if "large_airport" == rivi[0]:
                large_airport = large_airport + 1
            elif "medium_airport" == rivi[0]:
                medium_airport += 1
            elif "small_airport" == rivi[0]:
                small_airport += 1
            elif "closed" == rivi[0]:
                closed += 1
            elif "heliport" == rivi[0]:
                heliport += 1
        print(f"Suuria lentokenttiä {large_airport}, Keskikokoisia lentokenttiä {medium_airport}, pieniä lentokenttiä {small_airport},suljettu {closed}, Helikopterin laskeutumistasoja {heliport}")

lentokenttä_tyypit(input("Anna maakoodi: "))