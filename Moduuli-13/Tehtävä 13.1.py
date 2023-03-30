'''
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
'''

from flask import Flask, Response, jsonify, json

app = Flask(__name__)

def is_prime(n):
    vastaus = True
    for i in range(2, n):
        if n % i == 0:
            vastaus = False
    return vastaus

@app.route('/alkuluku/<int:n>', methods=['GET'])
def alkuluku(n):
    tulos = is_prime(n)
    vastaus = {
        "Number": n,
        "isPrime": tulos
    }
    return jsonify(vastaus)

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

