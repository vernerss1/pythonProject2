'''
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen
sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

'''

import mysql.connector

#muodostetaan yhteys tietokantaan
# Funktio hakee ja tulostaa pelaajan nimen ja paikan
# Funktio tarvitsee parametrnia pelaajan nimen.
# Funktio ei palauta mitään

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,    #Tietyille asioille on omat porttinsa esim. näppäimistö, internet
        database='flight_game',
        user='juuret',
        password='nine45',
        autocommit=True           # muutokset tietokantaan tehdään heti
        )

def lentokenttä_nimi_sijainti(ICAO):
    sql = "SELECT airport.name, country.name FROM airport, country " \
          "WHERE ident = '" + ICAO + "' AND country.iso_country = airport.iso_country"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f" ICAO koodia vastaava lentokenttä on  {rivi[1]} {rivi[0]}.")

lentokenttä_nimi_sijainti(input("Anna ICAO: "))
