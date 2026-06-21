import json

from config import get_token
from services.france_travail import get_jobs
from utils.menu import get_params_for_looking_jobs, take_choice_by_offer

def set_format_empty(libelle, value):
    if value is None or value == "" or value == {}:
        return f"{libelle} non disponible"
    
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False)

    return value

def get_details_offer(jobs):
    if jobs:
        for job in jobs["jobs"]:
            skills = job.get("skills", {})
            company = job.get("company", {})
            contract = job.get("contract", {})
            salary = job.get("salary", {})
            worktime = job.get("worktime", {})
            contact = job.get("contact", {})
            agency = job.get("agency", {})
            meta = job.get("meta", {})
      
            if contract.get('type') == "CDI" :

                print("\n" + "=" * 60)
                print(f"Titre                       : {set_format_empty('Titre', job.get('title'))}")
                print(f"Localisation                : {set_format_empty('Localisation', job.get('location'))}")
                print(f"Entreprise                  : {set_format_empty('Entreprise', job.get('company', {}).get('name'))}")
                print(f"Website                     : {set_format_empty('Website', company.get('website'))}")
                print(f"Type de contrat             : {set_format_empty('Type de contrat', contract.get('type'))}")
                print(f"Scrore de comptabilité      : {set_format_empty('Type de contrat', job.get('compatibility_score'))}")
                print(f"Compétences communes        : {set_format_empty('Type de contrat', job.get('compatibility_score'))}")
                print("=" * 60)
                
                print(f"Dates de mises à jour       : {set_format_empty('Dates de mises à jour', job.get('dates'))}")
                print(f"Description de l'offre      : {set_format_empty('Description', job.get('description'))}")

                print(f"Label du salaire            : {set_format_empty('Label du salaire', salary.get('label'))}")

                print(f"Durées de travail           : {set_format_empty('Durées de travail', worktime.get('raw'))}")

                print("\nCompétences :")
                for skill in skills:
                    print(f"- {skill.get('code')} | {skill.get('label')} | required={skill.get('required')}")

                print(f"Nom                         : {set_format_empty('Nom', contact.get('name'))}")
                print(f"Coordonnees1                : {set_format_empty('Coordonnees1', contact.get('coordonnees1'))}")
                print(f"Coordonnees2                : {set_format_empty('Coordonnees2', contact.get('coordonnees2'))}")
                print(f"Coordonnees3                : {set_format_empty('Coordonnees3', contact.get('coordonnees3'))}")

                print(f"Courriel                    : {set_format_empty('Courriel', agency.get('courriel'))}")
                print(f"Courriel                    : {set_format_empty('Courriel', agency.get('email_or_url'))}")
                
                print(f"Partenaire                  : {set_format_empty('Partenaire', meta.get('origineOffer'))}")
                
                take_choice_by_offer(job)

def manage_jobs():
    token = get_token()
    if token:
        print("Token récupéré :", token)
    else:
        print("Erreur lors de la récupération du token")
    # Données à fournir à params_job 
    params = get_params_for_looking_jobs()
    
    jobs = get_jobs(token, params)
    get_details_offer(jobs)
    
    return jobs