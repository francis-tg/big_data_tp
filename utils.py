def generate_pipeline(categorie_recherchee=None, limite=20):
    pipeline = []
    """ 
    En MongoDB, il existe toute une gamme d'opérateurs d'agrégation puissants pour manipuler et transformer les données lors des opérations d'agrégation. Voici quelques-uns des opérateurs couramment utilisés :

    $group : Regroupe les documents selon les critères spécifiés et permet d'effectuer des calculs sur les groupes de documents.

    $match : Filtre les documents pour ne garder que ceux qui correspondent aux critères spécifiés.

    $project : Permet de contrôler les champs qui seront inclus ou exclus dans les résultats de la requête.

    $sort : Trie les documents selon un ordre spécifié (croissant ou décroissant) en fonction des valeurs d'un ou plusieurs champs.

    $limit et $skip : Respectivement, limite le nombre de documents renvoyés dans les résultats et ignore un certain nombre de documents pour la pagination.

    $unwind : Décompose un tableau dans les documents en des documents individuels pour permettre des opérations d'agrégation sur ces éléments.

    $sum, $avg, $max, $min : Ces opérateurs effectuent des calculs d'agrégation tels que la somme, la moyenne, la valeur maximale et minimale respectivement.

    $project : Permet de contrôler l'inclusion ou l'exclusion de champs spécifiques dans les résultats.

    $lookup : Effectue une jointure entre deux collections pour récupérer des informations à partir d'une autre collection.

    $group : Permet de regrouper des documents et d'effectuer des opérations d'agrégation comme la somme, la moyenne, etc., sur les documents regroupés.

    Ces opérateurs sont souvent utilisés ensemble dans une pipeline d'agrégation pour filtrer, regrouper, trier et calculer des statistiques sur les données stockées dans MongoDB. Chaque opérateur offre une fonctionnalité spécifique pour manipuler et transformer les données selon vos besoins. 
    """

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
                },  # Calcule le revenu total pour chaque catégorie en multipliant la quantité par le prix unitaire (les fonctions d'aggrégation)
                "valeurs": {
                    "$push": {
                        "valeur_max": "$valeur_max",
                        "valeur_moyenne": "$valeur_moyenne",
                    }
                },
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
                    "valeur_max": {"$max": "$total_revenu"},
                    "valeur_moyenne": {"$avg": "$total_revenu"},
                }
            }
        )
    if limite is not None:
        limit_stage = {
            "$limit": limite  # Limite le nombre de résultats renvoyés par le pipeline
        }
        pipeline.append(limit_stage)
    return pipeline


def execute_pipeline(collection, pipeline): #exécute le le pipeline
    results = collection.aggregate(pipeline)
    return list(results)


def groupedData(data):
    grouped_data = {"categorie": [], "quantite": []}

    for item in data:
        grouped_data["categorie"].append(item["categorie"])
        grouped_data["quantite"].append(item["quantite"])
    return grouped_data
