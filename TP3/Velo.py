hdeb=int(input('saisire l"heures de début de la location :'))
hfin=int(input('saisire l"heures de fin de la location :'))
heur=int(hfin-hdeb)
loc1=heur
loc2=heur*2
lorel=heur

while (hdeb < 0 or hdeb > 24 or hfin<0 or hfin>24 or hfin<=hdeb):
    print('Les heurs ne sont pas valide !!!')
    hdeb = int(input('saisire l"heures de début de la location: '))
    hfin = int(input('saisire l"heures de fin de la location :'))
    heur =int (hfin - hdeb)


if hdeb < 7:
    if hfin < 7:
        t1 = hfin - hdeb
        prix = t1
        print("{} heure(s) au tarif de 1.0 euro(s)".format(t1))
        print("Le montant total sera de {}€".format(prix))
    elif hfin < 17:
        t1 = (7 - hdeb)
        t2 = (hfin - 7)
        prix = (t1) + (t2)
        print("{} heure(s) au tarif de 1.0 euro(s)".format(t1))
        print("{} heure(s) au tarif de 2.0 euro(s)".format(t2))
        print("Le montant total sera de {}€".format(prix))

    else:
        t1 = (7 - hdeb) + (hfin - 17)
        t2 = 10
        prix = (t1) + (t2)
        print("{} heure(s) au tarif de 1.0 euro(s)".format(t1))
        print("{} heure(s) au tarif de 2.0 euro(s)".format(t2))
        print("Le montant total sera de {}€".format(prix))

elif hdeb < 17:
    if hfin < 17:
        t2 = hfin - hdeb
        prix = t2
        print("{} heure(s) au tarif de 2.0 euro(s)".format(t2))
        print("Le montant total sera de {}€".format(prix))
    else:
        t2 = 17 - hdeb
        t1 = hfin - 17
        prix = (t1) * 1 + (t2) * 2
        print("{} heure(s) au tarif de 1.0 euro(s)".format(t1))
        print("{} heure(s) au tarif de 2.0 euro(s)".format(t2))
        print("Le montant total sera de {}€".format(prix))
else:
    t1 = hfin - hdeb
    prix = t1 * 1
    print("{} heure(s) au tarif de 1.0 euro(s)".format(t1))
    print("Le montant total sera de {}€".format(prix))

