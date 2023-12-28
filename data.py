import pandas as pd
from pymongo import MongoClient

# Lecture des données Excel dans un DataFrame pandas
df = pd.read_excel("donnee.xlsx")

# Connexion à MongoDB
client = MongoClient("localhost", 27017)
db = client["donnee_vente"]
collection = db["ventes"]

# Conversion des données du DataFrame pandas en dictionnaire pour l'insertion dans MongoDB
data = df.to_dict(orient="records")

# Insertion des données dans la collection MongoDB
collection.insert_many(data)

print("Données insérées avec succès dans MongoDB.")
