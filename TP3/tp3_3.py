import random
deviner = int(input("Deviner une valeur entre 0 et 100, entrez un nombre : "))
x = random.randint(0,100)
tour = 0
while deviner != x:
    if deviner > x:
        print("La valeur est supérieur à la valeur aléatoire")
        tour = tour +1
    print("Nombre de tour : ",tour,)

    if deviner < x:
        print("La valeur est inférieur à la valeur aléatoire")
        tour = tour +1
    deviner = int(input("Réessayer : "))
print("Vous avez réussi ! La valeur est bien : ", x)
