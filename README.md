# big_data_tp

# Installation et Configuration de Python avec MongoDB

Ce guide vous aidera à configurer un environnement Python avec une base de données MongoDB, à la fois en local et sur le cloud, et à installer les dépendances requises pour le projet à partir d'un fichier `requirements.txt`.

## Configuration de Python avec MongoDB en local

### Prérequis
Assurez-vous d'avoir installé Python et MongoDB sur votre machine.

### Étapes d'installation

1. **Installer Python :**
   - Téléchargez et installez Python depuis [python.org](https://www.python.org/downloads/).
   
2. **Installer MongoDB :**
   - Téléchargez MongoDB depuis [mongodb.com](https://www.mongodb.com/try/download/community) et suivez les instructions d'installation pour votre système d'exploitation.

3. **Installer les dépendances Python :**
   - Ouvrez un terminal.
   - Accédez au répertoire du projet.
   - Exécutez la commande suivante pour installer les dépendances à partir du fichier `requirements.txt` :
     ```
     pip install -r requirements.txt
     ```

4. **Lancer MongoDB en local :**
   - Démarrez le service MongoDB sur votre machine :
     ```
     mongod
     ```

## Configuration de Python avec MongoDB sur le Cloud

### Utilisation de MongoDB Atlas

1. **Créer un compte sur MongoDB Atlas :**
   - Accédez à [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) et créez un compte si vous n'en avez pas.

2. **Créer un cluster :**
   - Suivez les instructions pour créer un cluster MongoDB.

3. **Configurer l'accès à distance :**
   - Autorisez votre adresse IP à accéder au cluster MongoDB dans les paramètres de sécurité.

4. **Obtenir la chaîne de connexion :**
   - Accédez à votre cluster sur MongoDB Atlas.
   - Cliquez sur "Connect" et choisissez "Connect your application".
   - Copiez la chaîne de connexion fournie.

5. **Configurer votre application Python :**
   - Utilisez la chaîne de connexion copiée dans votre application Python pour vous connecter à MongoDB sur le cloud.

## Fichier `requirements.txt`

Le fichier `requirements.txt` contient les dépendances Python nécessaires pour le projet. Utilisez la commande `pip install -r requirements.txt` pour installer ces dépendances.
