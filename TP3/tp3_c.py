x=0
inf=0
sup1=0
sup2=0
for i in range (0, 10):
    n=int(input('Saisir 10 valeurs entre 0 et 20 : '))
    while 20 < n or 0 > n:
        n = int(input('Valeur incorecte Saisir un nombre entre 0 et 20 :'))
    if 0<=n<10:
        inf=inf+1
    if 10 <= n < 15:
        sup1 = sup1 + 1
    if 15 <= n <= 20:
        sup2=sup2+1
print(' Le nombre de valeurs inférieur strictement à 10 est :',inf)
print('Le nombre de valeurs supérieur à 10 et inférieur strictement à 15 est :',sup1)
print('Le nombre de valeurs supérieur à 15 est :',sup2)
