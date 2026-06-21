# structure des données

def normalize_job(raw):
    
    lieu = raw.get("lieuTravail", {})
    entreprise = raw.get("entreprise", {})
    salaire = raw.get("salaire", {})
    contact = raw.get("contact", {})
    agence = raw.get("agence", {})

    return {
        "id": raw.get("id"),

        "title": raw.get("intitule"),
        "description": raw.get("description"),

        "dates": {
            "created": raw.get("dateCreation"),
            "updated": raw.get("dateActualisation")
        },

        "location": {
            "label": lieu.get("libelle"),
            "city_code": lieu.get("commune"),
            "postal_code": lieu.get("codePostal"),
            "coordinates": {
                "lat": lieu.get("latitude"),
                "lon": lieu.get("longitude")
            }
        },

        "job": {
            "rome_code": raw.get("romeCode"),
            "rome_label": raw.get("romeLibelle"),
            "appellation": raw.get("appellationlibelle")
        },

        "company": {
            "name": entreprise.get("nom"),
            "description": entreprise.get("description"),
            "logo": entreprise.get("logo"),
            "website": entreprise.get("url"),
            "adapted": entreprise.get("entrepriseAdaptee")
        },

        "contract": {
            "type": raw.get("typeContrat"),
            "label": raw.get("typeContratLibelle"),
            "nature": raw.get("natureContrat"),
            "qualification": raw.get("qualificationLibelle")
        },

        "experience": {
            "required": raw.get("experienceExige") == "E",
            "label": raw.get("experienceLibelle"),
            "comment": raw.get("experienceCommentaire")
        },

        "salary": {
            "label": salaire.get("libelle"),
            "comment": salaire.get("commentaire"),
            "extras": [c.get("libelle") for c in salaire.get("listeComplements", [])]
        },

        "worktime": {
            "raw": raw.get("dureeTravailLibelle"),
            "label": raw.get("dureeTravailLibelleConverti"),
        },

        "skills": [
            {
                "code": c.get("code"),
                "label": c.get("libelle"),
                "required": c.get("exigence") == "S"
            }
            for c in raw.get("competences", [])
        ],

        "soft_skills": [
            q.get("libelle")
            for q in raw.get("qualitesProfessionnelles", [])
        ],

        "contact": {
            "name": contact.get("nom"),
            "address": " ".join(filter(None, [
                contact.get("coordonnees1"),
                contact.get("coordonnees2")
            ])),
            "application_url": contact.get("coordonnees3")
        },

        "agency": {
            "email_or_url": agence.get("courriel")
        },

        "meta": {
            "origineOffer": raw.get("origineOffre"),
            "positions": raw.get("nombrePostes"),
            "handicap_accessible": raw.get("accessibleTH"),
            "remote_policy": raw.get("deplacementLibelle"),
            "sector": raw.get("secteurActiviteLibelle"),
            "company_size": raw.get("trancheEffectifEtab"),
            "naf_code": raw.get("codeNAF"),
            "urgent": raw.get("offresManqueCandidats")
        }
    }
