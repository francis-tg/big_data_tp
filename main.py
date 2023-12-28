import pymongo

# Connexion à la base de données MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["donnee_vente"]
collection = db["ventes"]

# Exemple de pipeline d'agrégation
pipeline = [
    {"$group": {"_id": "$category", "total": {"$sum": "$amount"}}},
    {"$sort": {"total": -1}},
    {"$limit": 5},
]

# Exécution du pipeline d'agrégation
result_aggregation = collection.aggregate(pipeline)

print(list(result_aggregation))
# Traitement des résultats
for doc in result_aggregation:
    print(doc)

import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données depuis MongoDB vers pandas DataFrame
result_mongo = collection.find({},{"_id": 0, "category": 1, "amount": 1})
df = pd.DataFrame(list(result_mongo))

# Création d'un graphique (ici, un histogramme)
df.plot(kind="bar", x="category", y="amount", title="Montant par Catégorie")
plt.xlabel("Catégorie")
plt.ylabel("Montant")
plt.show()
