
# Django CRUD Simple

Une application web simple utilisant Django pour gérer les opérations CRUD (Créer, Lire, Mettre à jour, Supprimer) sur une entité.

## Table des matières

- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Prérequis

- [Python](https://www.python.org/downloads/) 3.6 ou supérieur
- [Django](https://www.djangoproject.com/) 4.0 ou supérieur

## Installation

1. Clone le dépôt :

    ```bash
    git clone https://github.com/Al-vallon/Crud-django.git
    ```

2. Accède au répertoire du projet :

    ```bash
    cd CRUD\crud
    ```

3. Crée et active un environnement virtuel :

    ```bash
    python -m venv env
    source env/bin/activate  # Sur Windows, utilise `env\Scripts\activate`
    ```

4. Installe les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Crée un fichier `.env` à la racine du projet et ajoute les variables d'environnement nécessaires. Exemple de configuration :

    ```
    DEBUG=True
    SECRET_KEY=ton-secret-key
    DATABASE_URL=sqlite:///db.sqlite3
    ```

2. Exécute les migrations pour configurer la base de données :

    ```bash
    python manage.py migrate
    ```

## Utilisation

1. Démarre le serveur de développement :

    ```bash
    python manage.py runserver
    ```

2. Accède à l'application via [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Contribuer

1. Fork le dépôt.
2. Crée une branche pour tes modifications :

    ```bash
    git checkout -b ma-nouvelle-fonctionnalité
    ```

3. Effectue tes modifications et commets-les :

    ```bash
    git add .
    git commit -m "Ajoute une nouvelle fonctionnalité"
    ```

4. Pousse ta branche :

    ```bash
    git push origin ma-nouvelle-fonctionnalité
    ```

5. Ouvre une Pull Request sur GitHub.

## Licence

Ce projet est sous la licence [MIT](LICENSE).


![example](https://github.com/user-attachments/assets/16831a67-c168-4304-9174-323c28c12a43)
