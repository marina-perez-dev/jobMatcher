# clés API
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# charger le .env
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
ROME_DIR = DATA_DIR / "wishlist"

WISHLIST_FILE = ROME_DIR / "wishlist.json"

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("Variables d'environnement manquantes !")

def get_token():
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "api_offresdemploiv2 o2dsoffre api_rome-metiersv1 nomenclatureRome api_rome-fiches-metiersv1" 
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    url = "https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=/partenaire"

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code != 200:
        print(response.text)
        return None
    return response.json().get("access_token")
