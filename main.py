import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import utils
from constant import DB_URL

# Connexion à la base de données MongoDB
client = pymongo.MongoClient(DB_URL)
db = client["donnee_vente"]
collection = db["ventes"]

pipeline = utils.generate_pipeline()
result_mongo = utils.execute_pipeline(pipeline=pipeline, collection=collection)
print(list(result_mongo))
df = pd.DataFrame(list(result_mongo))

# Création d'un graphique (ici, un histogramme)
df.plot(kind="bar", x="categorie", y="total_revenu", title="Analyse par Catégorie")
df.plot(kind="bar", x="categorie", y="total_quantite", title="Analyse par Catégorie")
df.plot(kind="bar", x="categorie", y="valeur_max", title="Analyse par Catégorie")
df.plot(kind="bar", x="categorie", y="valeur_moyenne", title="Analyse par Catégorie")
plt.xlabel("Catégorie")
plt.ylabel("Montant")
plt.show()
df.to_csv("./output/export.csv", index=False)
