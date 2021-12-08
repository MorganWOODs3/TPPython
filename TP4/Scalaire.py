n= int(input('Quelle est la taille de vos vecteurs [entre 1 et 10] ? : '))
nmax = 3
v1 = []
v2 = []
while n < 1 or n < nmax:
    n = int(input('Quelle est la taille de vos vecteurs [entre 1 et 10] ? : '))

print('saisir le premier vecteur :')

for i in range (n):
    x1 = int(input(f"v1[{i}]:"))
    v1.append(x1)

print('saisir le deuxième vecteur :')
for i in range (n):
    x2 = int(input(f"v2[{i}]:"))
    v2.append(x2)

sclaire= 0
for i in range(n):
    sclaire=v1[i]*v2[i]+sclaire
print('Le produit scalaire de v1 et v2 est :',sclaire)