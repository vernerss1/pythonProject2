'''
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
Laske etäisyys geopy-kirjaston avulla:

'''

import mysql.connector


yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='juuret',
        password='nine45',
        autocommit=True
        )

from geopy import distance
def lentokenttien_etäisyys_1(ICAO):
        sql = 'SELECT latitude_deg, longitude_deg ' \
        'FROM airport WHERE airport.ident = "' + ICAO + '"'
        #print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount > 0:
                for rivi in tulos:
                        return rivi[0], rivi[1]


paikka1 = lentokenttien_etäisyys_1(input("Anna ICAO:"))
paikka2 = lentokenttien_etäisyys_1(input("Anna ICAO: "))
print(f" Näiden etäisyys {distance.distance(paikka1, paikka2).km}km")


