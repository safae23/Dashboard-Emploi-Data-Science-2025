import requests

client_id = ""
client_secret = ""



token_url = "https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=/partenaire"

payload = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    'scope': 'o2dsoffre api_offresdemploiv2'
}

headers = {"Content-Type": "application/x-www-form-urlencoded"}

try:
    response = requests.post(token_url, data=payload, headers=headers)
    print("Status code :", response.status_code)
    print("Réponse brute :", response.text)
    response.raise_for_status()
    token = response.json().get("access_token")
    print("Token :", token)
except requests.exceptions.RequestException as e:
    print("Erreur :", e)
