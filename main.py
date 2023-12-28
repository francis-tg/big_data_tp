import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import utils



# Connexion à la base de données MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["donnee_vente"]
collection = db["ventes"]

pipeline = utils.generate_pipeline()
result_mongo = utils.execute_pipeline(pipeline=pipeline, collection=collection)
# print(list(result_mongo))
df = pd.DataFrame(list(result_mongo))

# Création d'un graphique (ici, un histogramme)
df.plot(kind="bar", x="categorie", y="total_revenu", title="Analyse par Catégorie")
plt.xlabel("Catégorie")
plt.ylabel("Montant")
plt.show()
