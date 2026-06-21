import json
import sys
import requests
from config import get_token
from services.rome_service import search_rome
from utils.menu import choose_rome_code
from utils.rome_utils import load_rome_local

file_path = "data/rome/skills.json"

# Charger mon fichier json avec mes compétences
def charge_file_skills(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []

def save_skills(file_path, skills):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(skills, f, ensure_ascii=False, indent=4)

def get_Code_ROME():
    metiers = load_rome_local()
    return choose_rome_code(metiers)

def get_skills_by_code_ROME(code):

    url = f"https://api.francetravail.io/partenaire/rome-fiches-metiers/v1/fiches-rome/fiche-metier/{code}"
    querystring = {
        "champs": "code,groupessavoirs(savoirs(libelle,code),categoriesavoirs(libelle,code))"

    }

    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
       return response.json()
    else:
        return None

def afficher_menu_competence():
    print("\nQue veux-tu faire ?")
    print("1 - Ajouter à mes compétences")
    print("2 - Passer à la compétence suivante")
    print("3 - Quitter")
    return input("\nTon choix : \n")

def verify_already_save(code_savoir, libelle):
    skills = charge_file_skills(file_path)

    for skill in skills:
        if skill['code'] == code_savoir and skill['libelle'] == libelle:
            return True

    return False

def get_list_skills_by_ROME():
    keyword = input("Recherche métier : ").strip()

    if not keyword:
        print("Aucun métier saisi.")
        return

    results = search_rome(keyword)

    if not results:
        print("Aucun résultat trouvé.")
        return

    code = choose_rome_code(results)

    if not code:
        print("Aucun code ROME sélectionné.")
        return

    data = get_skills_by_code_ROME(code)
    groupes = data.get("groupesSavoirs", [])

    if not groupes:
        print("Aucune compétence trouvée pour ce code ROME.")
        return

    for groupe in groupes:
        savoirs = groupe.get("savoirs", [])

        for savoir in savoirs:
            code_savoir = savoir.get("code", "Code non disponible")
            libelle = savoir.get("libelle", "Libellé non disponible")

            print("\n" + "-" * 50)
            print(f"Code    : {code_savoir}")
            print(f"Libellé : {libelle}")
            print("-" * 50)

            while True:
                choice = afficher_menu_competence()

                if choice == "1":
                    try:
                        if not verify_already_save(code_savoir, libelle):
                            add_New_Skill(code_savoir, libelle)
                            print("Compétence ajoutée")
                        else:
                            print("Compétence déjà présente")
                    except Exception as e:
                        print("Erreur :", e)
                    break

                elif choice == "2":
                    break

                elif choice == "3":
                    print("Fin du programme")
                    sys.exit()

                else:
                    print("Choix invalide, réessaie")


def add_New_Skill(code, libelle):
    skills = charge_file_skills(file_path)

    if skills is None:
        skills = []

    new_skill = {
        "code": code,
        "libelle": libelle
    }

    skills.append(new_skill)

    save_skills(file_path, skills)

    print("Compétence ajoutée avec succès !")
    
def manage_skills(): 
    while True:
        print("\nQue veux-tu faire ?")
        print("1 - Sélectionner un domaine de compétences")
        print("2 - Quitter")
        
        choice = input("\nTon choix : \n")
        if choice == "1":
            try:
                get_list_skills_by_ROME()
            except Exception as e:
                print("Erreur :", e)
        elif choice == "2":
            print("Fin du programme")
            sys.exit()
        else:
            print("Choix invalide, réessaie") 