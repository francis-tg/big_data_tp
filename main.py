import pymongo
import pandas as pd
import matplotlib.pyplot as plt


def groupedData(data):
    grouped_data = {"Catégorie": [], "quantite": []}

    for item in data:
        grouped_data["Catégorie"].append(item["Catégorie"])
        grouped_data["quantite"].append(item["quantite"])
    return grouped_data


# Connexion à la base de données MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["donnee_vente"]
collection = db["ventes"]

df = pd.read_excel("donnee.xlsx")
# Chargement des données depuis MongoDB vers pandas DataFrame
result_mongo = collection.find({}, {"_id": 0, "Catégorie": 1, "quantite": 1})
# print(list(result_mongo))
df = pd.DataFrame(groupedData(list(result_mongo)))

# Création d'un graphique (ici, un histogramme)
df.plot(kind="bar", x="Catégorie", y="quantite", title="Montant par Catégorie")
plt.xlabel("Catégorie")
plt.ylabel("Montant")
plt.show()
