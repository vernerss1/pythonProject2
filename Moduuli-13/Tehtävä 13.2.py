'''
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
'''

from flask import Flask, Response, jsonify, json

import mysql.connector

app = Flask(__name__)

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='l44k252',
    autocommit=True
)

def lentokenttä_nimi_sijainti(ICAO):
    sql = "SELECT airport.name, airport.municipality FROM airport WHERE ident = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (ICAO,))
    tulos = cursor.fetchone()
    if tulos:
        nimi, kaupunki = tulos
        return {"ICAO": ICAO, "Name": nimi, "Municipality": kaupunki}
    else:
        return {"error": "Lentokenttää ei löytynyt"}

@app.route('/kenttä/<ICAO>', methods=['GET'])
def hae_kenttä(ICAO):
    tulos = lentokenttä_nimi_sijainti(ICAO)
    if 'error' in tulos:
        jsonvast = json.dumps(tulos)
        return Response(response=jsonvast, status=404, mimetype="application/json")
    else:
        jsonvast = json.dumps(tulos)
        return Response(response=jsonvast, status=200, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(port=3000, debug=True)