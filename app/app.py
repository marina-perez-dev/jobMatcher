import sys

from services.jobs_service import manage_jobs
from services.skill_service import manage_skills
from services.wishlist_service import access_to_wish_list

def run_app():
    while True:
        print("\nFaites un choix ?")
        print("1 - Accéder aux favoris")
        print("2 - Accéder aux offres de france travail")
        print("3 - Renseigner mes compétences")
        print("4 - Quitter")
        choice = input("\nTon choix : \n")
        if choice == "1":
            access_to_wish_list()
            break
        elif choice == "2":
            manage_jobs()
            break 
        elif choice == "3":
            manage_skills()
            break
        elif choice == "4":
            print("Fin du programme")
            sys.exit()
        else:
            print("Choix invalide, réessaie") 
