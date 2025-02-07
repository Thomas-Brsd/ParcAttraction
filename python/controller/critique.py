import request.request as req

# Ajouter ou mettre à jour une critique
def add_critique(data):
    print(data, flush=True)
    if (not "nom" in data or data["nom"] == ""):
        return False
    
    if (not "texte" in data or data["texte"] == ""):
        return False

    if (not "note" in data or data["note"] is None):
        return False

    if (not "attraction_id" in data or data["attraction_id"] is None):
        return False

    if ("critique_id" in data and data["critique_id"]):
        requete = f"UPDATE critique SET nom='{data['nom']}', texte='{data['texte']}', note={data['note']} WHERE critique_id = {data['critique_id']}"
        req.insert_in_db(requete)
        id = data['critique_id']
    else:
        requete = "INSERT INTO critique (nom, texte, note, attraction_id) VALUES (?, ?, ?, ?);"
        id = req.insert_in_db(requete, (data["nom"], data["texte"], data["note"], data["attraction_id"]))

    return id

# Récupérer toutes les critiques
def get_all_critique():
    json = req.select_from_db("SELECT * FROM critique")
    
    return json

# Récupérer une critique spécifique par son id
def get_critique(id):
    if (not id):
        return False

    json = req.select_from_db("SELECT * FROM critique WHERE critique_id = ?", (id,))

    if len(json) > 0:
        return json[0]
    else:
        return []

# Supprimer une critique
def delete_critique(id):
    if (not id):
        return False

    req.delete_from_db("DELETE FROM critique WHERE critique_id = ?", (id,))

    return True
