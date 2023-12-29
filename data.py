import pandas as pd
from pymongo import MongoClient
from constant import DB_URL
# Lecture des données Excel dans un DataFrame pandas
df = pd.read_excel("./files/RandomData.xlsx")
# Connexion à MongoDB
client = MongoClient(DB_URL)
db = client["donnee_vente"]
collection = db["ventes"]

# Conversion des données du DataFrame pandas en dictionnaire pour l'insertion dans MongoDB
data = df.to_dict(orient="records")
new_data = []
for d in data:
    sd = {**d, "total": d["quantite"] * d["prix_unitaire"]}
    new_data.append(sd)

collection.insert_many(new_data)

pipeline = [
    {"$group": {"_id": "$category", "total": {"$sum": "$amount"}}},
    {"$sort": {"total": -1}},
    {"$limit": 5},
]

