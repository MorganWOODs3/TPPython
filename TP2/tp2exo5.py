a=int(input('Saisir un nombre entier:'))

if a > 0 and a % 2 == 0:
     print('Le nombre', a, ' est positive et paire')
elif a > 0:
     print('Le nombre', a, 'est positive et impaire')
elif a < 0 and a % 2 == 0:
     print('Le nombre', a, 'est negative et paire')
elif a == 0:
    print('Le nombre', a, ' est zero')
else:
    print('Le nombre', a, ' est negative et impaire')
