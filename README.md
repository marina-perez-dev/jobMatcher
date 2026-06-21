# jobMatcher

> Recherche intelligente d’offres d’emploi via l’API France Travail, directement depuis le terminal.

***

## Présentation

**jobMatcher** est une application Python en ligne de commande (CLI) qui permet de rechercher des offres d’emploi à partir d’un simple **mot-clé métier** (ex : *développeur*).

L’application guide ensuite l’utilisateur via une **navigation interactive** pour sélectionner un métier associé à un **code ROME**, puis affiche les offres correspondantes, triées du **plus récent au plus ancien**.

***

## Fonctionnement

```text
Mot-clé métier (ex : développeur)
        ↓
Suggestions de métiers (codes ROME)
        ↓
Navigation paginée (+ / -)
        ↓
Sélection d’un métier
        ↓
Récupération des offres via API France Travail
        ↓
Interaction utilisateur (wishlist, navigation, etc.)
```

***

## Démo - Interface CLI

### Recherche métier

```
Résultats 1 à 10 / 3654

0 - M1889 | Développeur IA
1 - M1805 | Développeur IOT
2 - M1855 | Développeur web
...
```

### Actions disponibles

```
+ → Page suivante
- → Page précédente
0-9 → Sélectionner un métier
```

***

## Consultation des offres

Chaque offre affiche :

* Titre
* Localisation
* Entreprise
* Type de contrat
* Description
* Date de mise à jour

Tri :

> **du plus récent au plus ancien**

***

## Menu interactif des offres

```
1 - Ajouter à la wishlist
2 - Passer à l'offre suivante
3 - Quitter
```

***

## Fonctionnalités

✅ Recherche par mot-clé métier  
✅ Suggestions dynamiques de codes ROME  
✅ Navigation paginée fluide  
✅ Affichage détaillé des offres  
✅ Tri par date (récent → ancien)  
✅ Gestion des favoris (wishlist)

***

## Gestion des favoris

* Ajouter une offre
* Consulter les favoris
* Supprimer une offre
* Accéder au lien pour postuler
* Naviguer entre les offres sauvegardées

***

## Technologies
* Python 3.10 ou supérieur
* API France Travail IO
* Interface CLI interactive

***

## Installation & mise en place

### 1. Cloner le projet

```bash
git clone https://github.com/marina-perez-dev/jobMatcher.git
cd jobMatcher
```

***

### 2. Créer l’environnement virtuel

```bash
python -m venv .venv_job_matcher
```

***

### 3. Activer l’environnement

#### Windows (PowerShell)

```powershell
.\.venv_job_matcher\Scripts\Activate.ps1
```

Si tu as une erreur de sécurité :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

***

#### Linux / Mac

```bash
source .venv_job_matcher/bin/activate
```

***

### 4. Installer les dépendances

Si un fichier `requirements.txt` est présent :

```bash
pip install -r requirements.txt
```

Sinon (version actuelle du projet), installe manuellement :

```bash
pip install requests
```

(*adapter selon tes dépendances réelles*)

***

## Configuration API France Travail

Afin d’utiliser les fonctionnalités de recherche d’offres, tu dois disposer d’un accès à l’API **France Travail IO**.

### 1. Créer un compte développeur

1. Crée un compte sur le portail partenaire :

<https://francetravail.io/>

2. Crée une application

3. Récupère tes identifiants :

* `CLIENT_ID`
* `CLIENT_SECRET`

***

### 2. Configurer les scopes nécessaires

Lors de la configuration de ton application, assure-toi d’activer les scopes suivants :

```
api_offresdemploiv2
o2dsoffre
api_rome-metiersv1
nomenclatureRome
api_rome-fiches-metiersv1
```

Ces scopes permettent :

* la recherche d’offres
* l’accès aux données ROME
* la récupération des fiches métiers et compétences

***

### 3. Créer le fichier `.env`

À la racine du projet, crée un fichier `.env` :

```env
CLIENT_ID=ton_client_id
CLIENT_SECRET=ton_client_secret
```

***

### 4. Sécurité

Ne partage **jamais** ce fichier `.env` :

Ajoute-le dans ton `.gitignore` :

```gitignore
.env
```

***

### 5. Génération du token

L’application utilise automatiquement un token OAuth2 via la fonction suivante :

```python
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
```

***

### Résultat

Une fois configuré :

L’application peut :

* récupérer les offres d’emploi
* interroger les données ROME
* afficher les compétences

***

## Lancer le projet

```bash
python main.py
```

***

## Exemple d’utilisation

1. Lancer le programme
2. Entrer un métier :

```
développeur
```

3. Naviguer dans les suggestions :

```
+ / -
```

4. Choisir un métier :

```
2
```

5. Parcourir les offres et interagir

***

## Structure du projet (exemple)

```bash
jobMatcher/
│
├── main.py
├── config.py
├── .env
├── README.md
├── requirements.txt
│
├── data/
│   ├── rome/
│   │   ├── rome_metiers.json
│   │   ├── skills.json
│   │   └── ROME_Arborescence.xlsx
│   └── wishlist/
│       └── wishlist.json
│
├── models/
│   └── schema.py
│
├── services/
│   ├── job_service.py
│   ├── rome_service.py !!
│   ├── skill_service.py
│   └── wishlist_service.py
│
├── filters/
│   ├── datetime_filter.py
│   └── skill_filter.py
│
└── utils/
    ├── display.py
    ├── menu.py
    └── helpers.py
```

***

## Limitations

* Interface uniquement CLI
* Peu de filtres avancés (salaire, distance…)
* Dépendance à l’API France Travail

***

## Améliorations possibles

À venir :

* Filtres avancés (salaire, localisation, contrat)
* Interface CLI améliorée (couleurs, UX)
* Sauvegarde persistante
* Version web ou application mobile
* Matching compétences ↔ offres

***

## Auteur

Projet développé par **\[Ton Nom]**

***

## Licence

MIT License

***