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


while True:
    print("--------------------------------")
    print("Calculatrice simple : ")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5.Quiter")
    print("--------------------------------")

    choix = int(input("choisissez votre opperation : "))

    if choix == 5:
        print("Fermeture de la calculatrice !")
        break

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
