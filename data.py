import requests
import pandas as pd
import re

token = ""
url = "https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

metiers = [
    "Data Scientist",
    "Data Engineer",
    "Data Analyst",
    "Business Analyst",
    "BI Analyst",
    "Data Architect",
    "Machine Learning Engineer",
    "AI Engineer",
    "Deep Learning Engineer",
    "Statisticien",
    "Consultant Data",
    "Big Data Engineer",
    "Data Manager",
    "Data Product Manager",
    "Cloud Data Engineer",
    "Data Consultant",
    "Data Developer",
    "Data Steward",
    "DataOps Engineer",
    "MLOps Engineer"
]

competence_keywords = [
    "python", "r", "scala", "java", "c++", "c#", "go", "typescript",
    "sql", "mysql", "postgresql", "oracle", "nosql", "mongodb", "snowflake", "bigquery", "redshift",
    "pandas", "numpy", "scipy", "matplotlib", "seaborn", "scikit-learn", "tensorflow", "pytorch",
    "keras", "xgboost", "lightgbm", "power bi", "tableau", "qlik", "looker", "superset", "datastudio",
    "excel", "google sheets", "aws", "azure", "gcp", "google cloud", "docker", "kubernetes", 
    "terraform", "airflow", "mlflow", "databricks", "jenkins", "git", "github", "gitlab", 
    "ci/cd", "hadoop", "spark", "hive", "pig", "flink", "kafka", "data visualization", 
    "machine learning", "deep learning", "nlp", "ia", "artificial intelligence", "big data", 
    "data mining", "statistiques", "modelisation", "feature engineering", "etl", "pipeline", 
    "dash", "streamlit", "api", "json", "rest", "agile", "jira", "scrum"
]

# fonction de détection du niveau d’expérience
def detect_niveau(poste, description):
    text = (poste + " " + description).lower()
    if any(x in text for x in ["stage", "stagiaire", "internship"]):
        return "Stage"
    elif any(x in text for x in ["alternance", "apprenti", "contrat pro"]):
        return "Alternance"
    elif any(x in text for x in ["junior", "débutant", "entry level"]):
        return "Junior"
    elif any(x in text for x in ["senior", "confirmé", "expérimenté", "lead", "expert"]):
        return "Senior"
    else:
        return "Non spécifié"

all_offres = []

for metier in metiers:
    params = {"motsCles": metier, "range": "0-120"}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        offres = data.get("resultats", [])
        print(f"{len(offres)} offres récupérées pour : {metier}")

        for offre in offres:
            poste = offre.get("intitule", "").strip()
            lieu = offre.get("lieuTravail", {}).get("libelle", "").strip()
            salaire = offre.get("salaire", {}).get("libelle", "").strip()
            experience = offre.get("experienceLibelle", "").strip()
            entreprise = offre.get("entreprise", {}).get("nom", "").strip()
            description = offre.get("description", "")
            description = description.replace("\n", " ").replace("\r", " ").strip()

            competences_api = [c.get("libelle") for c in offre.get("competences", []) if c.get("libelle")]
            desc_lower = description.lower()
            competences_detectees = [kw for kw in competence_keywords if kw in desc_lower]
            competences_finales = list(set(competences_api + competences_detectees))

            # Détection du niveau
            niveau = detect_niveau(poste, description)

            all_offres.append({
                "Métier": metier,
                "Entreprise": entreprise or "Non spécifié",
                "Poste": poste or "Non spécifié",
                "Niveau": niveau,
                "Lieu": lieu or "Non spécifié",
                "Salaire": salaire or "Non spécifié",
                "Expérience": experience or "Non spécifié",
                "Compétences": ", ".join(competences_finales) if competences_finales else "Non spécifiées",
                "Description": description[:500]
            })

    except requests.exceptions.RequestException as e:
        print(f"Erreur pour {metier} :", e)

df = pd.DataFrame(all_offres)
df.drop_duplicates(subset=["Poste", "Entreprise", "Lieu"], inplace=True)
df = df[df["Description"].str.len() > 30]

df.to_csv("offres_data_jobs_france_2025_niveau.csv", index=False, encoding="utf-8-sig")

print(f"Export terminé : {len(df)} offres valides sauvegardées dans 'offres_data_jobs_france_2025_niveau.csv'")
