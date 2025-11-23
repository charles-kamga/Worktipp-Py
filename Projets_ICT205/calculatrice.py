import math as mt


def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    return "Division par 0 impossible"


def puissance(a,b):
    if b == 0:
        return 1
    else:
        return a**b

def racine(a):
    return mt.sqrt(a)


def modulo(a,b):
    if b == 0:
        return "division par 0 impossible"
    else:
        return a%b

#commentaire pour tester le push via GNU Pycharm
while True:
    print("--------------------------------")
    print("Calculatrice simple : ")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Puissance")
    print("6. Racine")
    print("7. Modulo")
    print("8. Quitter")
    print("--------------------------------")

    choix = int(input("choisissez votre opperation : "))

    if choix == 8:
        print("Fermeture de la calculatrice !")
        break


    elif choix == 6:
        nb1 = float(input("Entrer le nombre : "))
        print(f"({nb1})^½ = {racine(nb1)}")
    else:
        nb1 = float(input("Entrer le premier nombre : "))
        nb2 = float(input("Entrer le deuxieme nombre : "))

    if choix == 1 :
        print(f"{nb2} + {nb1} = {addition(nb1,nb2)}")

    elif choix == 2:
        print(f"{nb2}-{nb1} = {soustraction(nb1, nb2)}")

    elif choix == 3:
        print(f"{nb2}x{nb1} = {multiplication(nb1, nb2)}")

    elif choix == 4:
        print(f"{nb2}/{nb1} = {division(nb1, nb2)}")

    elif choix == 5:
        print(f"{nb1}^{nb2} = {puissance(nb1,nb2)}")

    elif choix == 7:
        print(f"{nb1}={modulo(nb1,nb2)}[{nb2}]")

