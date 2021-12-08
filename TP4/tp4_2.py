nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []
ecart=0

for i in range(0,nombreEtudiants):
    x = int(input(f"Note etudiant {i} : "))
    while 0 > x or x > 20:
        print('valeur incorecteé')
        x = int(input(f"Note etudiant {i} : "))
    notes.append(x)
moyenne=sum(notes) / nombreEtudiants
ecart=notes[i]-moyenne
print('Moyenne de classe :', moyenne)
print('Numéro de l’Etudiant | note | ecart a la moyenne')
for i in range(nombreEtudiants):

    print(f"{i}" f"|" f"{notes[i]}" f"|" f"{ecart}")
