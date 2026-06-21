import requests
from models.schema import normalize_job
from services.Filters.datetime_filter import filter_by_date_time
from services.Filters.skill_filter import set_compatibility_between_skills
from services.skill_service import charge_file_skills

def normalize_response(api_response):

    jobs = api_response.get("resultats", [])

    filter_by_date_time(jobs)

    my_skills = charge_file_skills("data/rome/skills.json")
    personal_skill_codes = {
        s["code"]
        for s in my_skills
        if s.get("code")
    }

    enriched_jobs = []

    for job in jobs:
        try:
            competences = job.get("competences") or []

            listSkillsJob = [
                {
                    "code": c.get("code"),
                    "libelle": c.get("libelle", "")
                }
                for c in competences
                if c.get("code")
            ]

            score, common_skills = set_compatibility_between_skills(
                listSkillsJob,
                personal_skill_codes
            )

            normalized = normalize_job(job)

            normalized["compatibility_score"] = round(score, 2)
            normalized["common_skills"] = common_skills

            enriched_jobs.append(normalized)

        except Exception as e:
            print(f"Offre ignorée : {e}")
            continue

    return {"jobs": enriched_jobs}

# Récupération des offres
def get_jobs(token, params):
    url = "https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return normalize_response(response.json())
    else:
        return None

