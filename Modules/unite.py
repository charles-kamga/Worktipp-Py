# test sur les opperations

print(1+1)
print(10//3)
print(10/3)
print("====================")

#test sur les chaines : inversion et bns, les multiples variables
site = 'smartnskilled.com'

print(site[3])
print(f"{site}")
print(site)

site2 = 'udemy.com'

print(site2)
print(site[::-1])

x,y,z = 'Pivaut', '1', 'Propre'

print(x,z,y)

print("====================")

#palindrome
def palindrome(palin):
    if palin == (palin[::-1]):
        return print(f"'{palin}' est un palindrome")
    else:
        return print(f"'{palin}' n'est pas un palindrome")


mot = str(input("Entrer votre mot : "))
palindrome(mot)
print("====================")

#test sur les listes, inversion, et liste multidimensionnelles
liste = ['ceci','est','une','liste']
print(liste)
print("L,inverse de la liste : ")
# print (liste [::-1])

liste2Dim = [1,2],[2,4],[8,5],[40,6]

print(liste2Dim)
print((liste2Dim[2][0]),(liste2Dim[1][1]))
print(f"{liste2Dim[2][0]} est le valeur de l'element 0 du couple 1;")
print(f"{liste2Dim[1][1]} est la valeur de l'element 1 du couple 1")
print("======================================")

print("On definit une liste : ")
liste2 = [[5],[4],[8],[7],[2],[14],[18],[6]]
print("avant ajout : ")
print(liste2)
liste2.append([20])
print("apres ajout: ")
print(liste2)
liste2.insert(1,[1])
print("apres insertion à l'index 1 de 1, on a : ")
print(liste2)
liste2.remove([2])
print("on vient de retirer l'element 2 de la liste : ")
print(liste2)
print("On vient de retirer l'element à l'index 2 de la liste : 4")
liste2.pop(2)
print(liste2)
print("On veut afficher l'element qui est à l'index 3 : ")
print(liste2[3])
print("On veut connaitre l'index d'un element, de l'element 7 par exemple : ")
print(liste2.index([7]))

fruits = ['pomme','tomate','banane','orange']
for fruit in fruits:
    print(fruit)
else : print("\nPlus de fruits dans le panier")

for i in range(3):
    print(i)
print("fin\n")

prenom = "John"
for lettre in prenom:
    print(lettre)

for (pk,name) in [(1,'john'),(2,'The'),(3,'Harvester')]:
    # print(pk,name)
    print(name)
    print(pk)
    print(pk,name)

nombre = 0
for nombre in range(10):
    if nombre == 5:
        break
    print(f'Le Nombre est {nombre}')
print('En dehors de la boucle')

for i in range(10):
        if i==5:
            continue
        print(f"Le nombre est : {i}")
print("En dehors de la boucle")

for i in range(10):
    if i==5:
        pass
    print(i)
print("En dehors de la boucle")

# ========================================================================
# test palindrome
# ========================================================================

def palindrome(palin):
    if palin == (palin[::-1]):
        return print(f"'{palin}' est un palindrome")
    else:
        return print(f"'{palin}' n'est pas un palindrome")

mot = input("Entrer le mot : ")
palindrome(mot)



# ========================================================================
# Test Gestion des etudiants
# ========================================================================