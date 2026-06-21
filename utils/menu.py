
import sys

from services.rome_service import paginate_results, search_rome
from services.wishlist_service import add_to_my_wish_list
from utils.input_utils import ask_input
from utils.rome_utils import load_rome_local


def choose_rome_code(results):
    page = 0
    page_size = 10

    while True:
        page_items, start, end, total = paginate_results(results, page, page_size)

        if not page_items:
            print("Fin des résultats.")
            return None

        print("\n" + "=" * 50)
        print(f"Résultats {start + 1} à {min(end, total)} / {total}\n")

        for i, metier in enumerate(page_items):
            print(f"{i} - {metier['code']} | {metier['libelle']}")

        print("\nActions :")
        print("+ - suivant")
        print("- - précédent")
        print("0-9 - sélectionner")

        choice = input("Ton choix : ").strip()

        if choice == "+":
            page += 1

        elif choice == "-" and page > 0:
            page -= 1

        elif choice.isdigit():
            index = int(choice)

            if 0 <= index < len(page_items):
                return page_items[index]["code"]

            print("Choix invalide")

        else:
            print("Entrée invalide")

def take_choice_by_offer(job):
    while True:
        print("\nQue veux-tu faire ?")
        print("1 - Ajouter à la wishlist")
        print("2 - Passer à l'offre suivante")
        print("3 - Quitter")
        choice = input("\nTon choix : \n")
        if choice == "1":
            try:
                add_to_my_wish_list(job)
            except Exception as e:
                print("Erreur :", e)
            break  # passer à l’offre suivante
        elif choice == "2":
            break  # passer directement
        elif choice == "3":
            print("Fin du programme")
            sys.exit()
        else:
            print("Choix invalide, réessaie") 


def get_params_for_looking_jobs():
    params = {}

    # 1. Recherche métier (comme skills)
    keyword = input("Recherche métier : ").strip()

    if not keyword:
        print("Aucun métier saisi.")
        return None

    results = search_rome(keyword)

    if not results:
        print("Aucun résultat trouvé.")
        return None

    # 2. Choix du code ROME filtré
    code = choose_rome_code(results)

    if not code:
        print("Aucun code ROME sélectionné.")
        return None

    params["codeROME"] = code

    # 3. Choix localisation
    print("\nRecherche par :")
    print("1 - Département (simple)")
    print("2 - Commune (avancé)")

    choice = input("Choix : ").strip()

    if choice == "1":
        params["departement"] = ask_input("Département")

    elif choice == "2":
        params["commune"] = ask_input("Code INSEE")
        params["distance"] = ask_input("Distance (km)", "int")

    else:
        print("Choix invalide")

    return params


