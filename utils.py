def generate_pipeline(categorie_recherchee=None, limite=20):
    pipeline = []

    if categorie_recherchee:
        pipeline.append(
            {
                "$match": {
                    "categorie": categorie_recherchee  # Filtre les documents par la catégorie spécifiée si une catégorie est fournie
                }
            }
        )

    pipeline.append(
        {
            "$group": {
                "_id": {"categorie": "$categorie", "nom": "$nom"},
                "total_quantite": {
                    "$sum": "$quantite"
                },  # Calcule la somme de la quantité pour chaque catégorie
                "total_revenu": {
                    "$sum": {"$multiply": ["$quantite", "$prix_unitaire"]}
                },  # Calcule le revenu total pour chaque catégorie en multipliant la quantité par le prix unitaire
            }
        }
    )

    if not categorie_recherchee:
        pipeline.append(
            {
                "$project": {
                    "_id": 0,  # Supprime le champ "_id" si toutes les catégories sont recherchées,
                    "categorie": "$_id.categorie",  # Ajoute le champ "categorie" dans les résultats
                    "nom": "$_id.nom",  # Ajoute le champ "nom" dans les résultats
                    "total_quantite": 1,  # Inclut le champ "total_quantite"
                    "total_revenu": 1,  # Inclut le champ "total_revenu",
                    "quantite": "$_id.quantite",
                }
            }
        )
    if limite is not None:
        limit_stage = {
            "$limit": limite  # Limite le nombre de résultats renvoyés par le pipeline
        }
        pipeline.append(limit_stage)
    return pipeline


def execute_pipeline(collection, pipeline):
    results = collection.aggregate(pipeline)
    return list(results)


def groupedData(data):
    grouped_data = {"categorie": [], "quantite": []}

    for item in data:
        grouped_data["categorie"].append(item["categorie"])
        grouped_data["quantite"].append(item["quantite"])
    return grouped_data
