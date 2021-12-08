jour = int(input("Saisir jour du mois :"))

heure = int(input("Saisir l'heure du mois :"))

minute = int(input("Saisir minute du mois :"))
nbr_minute= (jour-1) *24*60 + heure*60 + minute
print("Le nombre de minute passer dans le mois",nbr_minute,)