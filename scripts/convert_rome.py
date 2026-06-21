
import pandas as pd
import json

# Charger le fichier Excel
df = pd.read_excel(
    "data/rome/ROME_Arborescence_principale_sept_2025.xlsx",
    sheet_name="Arbo Principale 18-09-2025",
    header=0
)

results = []

for _, row in df.iterrows():
    
    # Extraire les colonnes
    domaine = str(row.iloc[0]) if pd.notna(row.iloc[0]) else ""
    sous_domaine = str(row.iloc[1]) if pd.notna(row.iloc[1]) else ""
    code_partiel = str(row.iloc[2]) if pd.notna(row.iloc[2]) else ""
    libelle = str(row.iloc[3]) if pd.notna(row.iloc[3]) else ""

    # Filtrer les lignes valides
    if domaine and sous_domaine and code_partiel and libelle:
        
        # Construire le code ROME
        code = f"{domaine}{sous_domaine}{code_partiel}"

        results.append({
            "code": code,
            "libelle": libelle
        })

# Sauvegarde JSON
with open("data/rome/rome_metiers.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("JSON créé avec", len(results), "métiers")
