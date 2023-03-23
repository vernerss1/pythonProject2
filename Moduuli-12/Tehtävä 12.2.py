'''
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma,
joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen,
jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
'''

import json
import requests


hakusana = input("Anna kaupunging nimi: ")

pyyntö = "https://api.openweathermap.org/data/2.5/weather?q=" + hakusana + "&appid=193bad4b0ee03a30f3e61fb2605de6c3"

# Testaa tulostuva hakulause selaimella. Jos se palauttaa haluttua dataa, niin tämän koodin voi poistaa tai kommentoida
print("Nettiin lähtevä hakulause: ")
print(pyyntö)

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        lämpötila_asteina = json_vastaus['main']['temp'] - 273.15
        säätila = json_vastaus['weather'][0]['description']
        print (f"Säätila: {säätila}")
        print(f"Tuulen nopeus: {json_vastaus ['wind'] ['speed']} m/s")
        print(f"Lämpötila: {lämpötila_asteina:.2f} °C")

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")



