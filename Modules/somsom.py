from datetime import date
from unite import palindrome
import calculatrice
from unite import palindrome



def calcul_de_l_age(age):
    anne_naiss = float(input("Entrer votre anné de naissance : "))
    anne_actuelle = date.today().year
    age = anne_actuelle - anne_naiss
    return age

def menu_menu():
    print('===================================================')
    print("1. Calculatrice")
    print("2. Palindrome")
    print("3. Jeu du nombre magique")


#la boucle infinie (le while true);
#le menu pour le choix de l'utilisateur;
# la recupération de l'utilisateur;
# le dispatch pour le choix des execution.