
import json
import os

from config import WISHLIST_FILE

def verify_Json_file_Exist(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    else:
        return []

def update_status_offer(file_path, job_id, new_status):
    # Mettre à jour le status de l'offre à postuler
    content = verify_Json_file_Exist(file_path)
    
    print("job_id : ", job_id)
    for job in content:
        print("job.get('id') : ",job.get("id"))
        if job.get("id") == job_id:
            print("job['status']_1 : ", job["status"])
            job["status"] = new_status
        print("job['status']_2 : ", job["status"])
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False, indent=4)

def remove_offer_from_wish_list(file_path, job_id):
    content = verify_Json_file_Exist(file_path)

    new_content = [job for job in content if job.get("id") != job_id]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(new_content, f, ensure_ascii=False, indent=4)

def add_to_my_wish_list(job):
    # Charger contenu existant
    content = verify_Json_file_Exist(WISHLIST_FILE)
    
     # Vérifier si l'offre existe déjà
    exists = any(j.get("id") == job.get("id") for j in content)

    if not exists:
        job["status"] = "to_apply" # optionnel
        content.append(job)

        # Réécrire fichier
        with open(WISHLIST_FILE, "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False, indent=4)
        
        print("Offre ajoutée à la liste des favoris")
    else:
        print("Offre déjà présente dans la liste des favoris")
        
def access_to_wish_list():
    # Charger contenu existant
    content = verify_Json_file_Exist(WISHLIST_FILE)

    if not content:
        print("Aucune offre dans la wishlist.")
        return

    for offer in content:

        if offer.get("status") == "applied":
            continue

        print("\n" + "=" * 50)

        print("Titre        :", offer.get("title", "Non renseigné"))
        print("Entreprise   :", offer.get("company", {}).get("name", "Non renseigné"))
        print("Lieu         :", offer.get("location", {}).get("label", "Non renseigné"))
        print("Contrat      :", offer.get("contract", {}).get("type", "Non renseigné"))

        print("Salaire      :", offer.get("salary", {}).get("label", "Non renseigné"))
        print("Temps travail:", offer.get("worktime", {}).get("raw", "Non renseigné"))

        print("\nCompétences :")

        skills = offer.get("skills", [])

        if skills:
            for skill in skills:
                print("-", skill.get("label", "Non renseigné"))
        else:
            print("Aucune compétence renseignée")

        print("\nContact :") 
        print("Nom  :", offer.get("contact", {}).get("name", "Non renseigné"))
        print("Lien :", offer.get("contact", {}).get("application_url", "Non renseigné"))
        
        print("Lien Agence      :", offer.get("agency", {}).get("email_or_url", "Non renseigné"))
        print("Offre d'origine  :", offer.get("meta", {}).get("origineOffer", "Non renseigné"))

        print("\nStatut :", offer.get("status", "Non renseigné"))

        while True:

            print("\nActions disponibles :")
            print("1 - Marquer comme postulée")
            print("2 - Supprimer l'offre")
            print("3 - Offre suivante")
            print("4 - Quitter")

            choice = input("\nTon choix : \n").strip()

            if choice == "1":
                try:
                    update_status_offer(
                        WISHLIST_FILE,
                        offer.get("id"),
                        "applied"
                    )
                    print("Offre marquée comme postulée")
                except Exception as e:
                    print("Erreur :", e)

                break

            elif choice == "2":
                try:
                    remove_offer_from_wish_list(
                        WISHLIST_FILE,
                        offer.get("id")
                    )
                    print("Offre supprimée")
                except Exception as e:
                    print("Erreur :", e)

                break

            elif choice == "3":
                break

            elif choice == "4":
                print("Fin de la consultation.")
                return

            else:
                print("Choix invalide, réessaie.")
