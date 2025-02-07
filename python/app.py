from flask import Flask, jsonify, request
from flask_cors import CORS

import request.request as req
import controller.auth.auth as user
import controller.attraction as attraction
import controller.critique as critique  # Ajout de la gestion des critiques

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

# Attraction
@app.post('/attraction')
def addAttraction():
    print("okok", flush=True)
    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken

    json = request.get_json()
    retour = attraction.add_attraction(json)
    if (retour):
        return jsonify({"message": "Element ajouté.", "result": retour}), 200
    return jsonify({"message": "Erreur lors de l'ajout.", "result": retour}), 500

@app.get('/attraction')
def getAllAttraction():
    result = attraction.get_all_attraction()
    return result, 200

@app.get('/attraction/<int:index>')
def getAttraction(index):
    result = attraction.get_attraction(index)
    return result, 200

@app.delete('/attraction/<int:index>')
def deleteAttraction(index):

    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken

    json = request.get_json()
    
    if (attraction.delete_attraction(index)):
        return "Element supprimé.", 200
    return jsonify({"message": "Erreur lors de la suppression."}), 500

# Critique
@app.post('/critique')
def addCritique():
    print("okok critique", flush=True)
    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken

    json = request.get_json()
    retour = critique.add_critique(json)
    if (retour):
        return jsonify({"message": "Critique ajoutée.", "result": retour}), 200
    return jsonify({"message": "Erreur lors de l'ajout de la critique.", "result": retour}), 500

@app.get('/critique')
def getAllCritique():
    result = critique.get_all_critique()
    return result, 200

@app.get('/critique/<int:index>')
def getCritique(index):
    result = critique.get_critique(index)
    return result, 200

@app.delete('/critique/<int:index>')
def deleteCritique(index):

    # Fonction vérif token
    checkToken = user.check_token(request)
    if (checkToken != True):
        return checkToken

    json = request.get_json()
    
    if (critique.delete_critique(index)):
        return "Critique supprimée.", 200
    return jsonify({"message": "Erreur lors de la suppression de la critique."}), 500

# Login
@app.post('/login')
def login():
    json = request.get_json()

    if (not 'name' in json or not 'password' in json):
        result = jsonify({'messages': ["Nom ou/et mot de passe incorrect"]})
        return result, 400
    
    cur, conn = req.get_db_connection()
    requete = f"SELECT * FROM users WHERE name = '{json['name']}' AND password = '{json['password']}';"
    cur.execute(requete)
    records = cur.fetchall()
    conn.close()

    result = jsonify({"token": user.encode_auth_token(list(records[0])[0]), "name": json['name']})
    return result, 200
