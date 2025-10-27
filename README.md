# Dashboard Emploi Data Science France 2025

> **Analyse du marché de l’emploi en Data Science en France pour l’année 2025**, à partir des données récupérées via l’API officielle de France Travail et visualisées dans Power BI.

## Objectif du projet

Ce projet a pour but de :

* **Scraper les offres d’emploi** liées aux métiers de la Data Science en France à l’aide de l’API France Travail,
* **Analyser les tendances** : salaires moyens, répartition géographique, niveaux d’expérience, compétences les plus demandées,
* Et **visualiser les résultats** à travers un **dashboard interactif Power BI**.

## Technologies utilisées

| Domaine                 | Outils                                                                                                         |
| ----------------------- | -------------------------------------------------------------------------------------------------------------- |
| Langage                 | Python                                                                                                         |
| Requête API             | `requests`                                                                                                     |
| Manipulation de données | `pandas`, `re`, `json`                                                                                         |
| Export des données      | CSV (`utf-8-sig`)                                                                                              |
| Visualisation           | Power BI                                                                                                       |
| API                     | [API France Travail – Offres d’emploi](https://www.data.gouv.fr/dataservices/api-offres-demploi/) |

---

## Étapes du projet

### 1️⃣ Authentification à l’API France Travail

Obtention du **token OAuth2** grâce à `client_id` et `client_secret` :

---

### 2️⃣ Récupération des offres d’emploi

Une liste de **20 métiers liés à la Data Science** a été ciblée :

> Data Scientist, Data Engineer, Data Analyst, Machine Learning Engineer, Data Manager, BI Analyst, etc.

Chaque métier est recherché via l’API .

---

### 3️⃣ Extraction et nettoyage des données

Les informations extraites incluent :

* Métier, Entreprise, Lieu, Niveau d’expérience, Salaire, Description,
* Compétences détectées dans le texte (Python, SQL, Machine Learning, etc.)

---

### 4️⃣ Export des données

Les offres nettoyées sont enregistrées dans un fichier CSV :

---

### 5️⃣ Création du Dashboard Power BI

Les données exportées sont ensuite **visualisées dans Power BI** à travers plusieurs indicateurs .

## 🖼️ Aperçu du Dashboard

![Dashboard Data Science France 2025](data.pdf)

---

## 📊 Résultats clés

* Les métiers les plus demandés : **Data Engineer**, **Data Scientist**, **Data Analyst**
* Les villes les plus dynamiques : **Paris, Nantes, Lyon, Bordeaux**
* Les compétences les plus recherchées : **Python**, **SQL**, **Power BI**, **Machine Learning**, **AWS**
* La majorité des offres s’adressent à des **profils seniors ou confirmés**.
