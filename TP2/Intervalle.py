x=float(input('saisire un nombre reel :'))
if (x>=2 and x<3) or (x > 0 and x <= 1) or (x>=-10 and x<=-2):
        print(x,'appartient à I')
else:
    print(x,'n"appartient pas  à I')





if(hdeb < 7):
    if(hfin < 7):
        prix = hfin - hdeb
    elif hfin<17:
        prix= 7-hdeb+(hfin-7)*2
    else:
        prix=7-hdeb+10*2+hfin-17
elif (hdeb < 17):
    if(hfin<17):
        prix=(hfin-hdeb)*2
    else:
        prix = (17-hdeb)*2 + hfin-17
else:
    prix = hfin-hdeb
print('Le montant total à payer est de',prix,' euro(s)')






while (hdeb < 0 or hdeb > 24 or hfin<0 or hfin>24 or hfin<=hdeb):
    print('Les heurs ne sont pas valide !!!')
    hdeb = int(input('saisire l"heures de début de la location: '))
    hfin = int(input('saisire l"heures de fin de la location :'))
    heur =int (hfin - hdeb)
if hdeb<7 or hfin>=17:
    print(heur,'heure(s) au tarif horaire de 2.0 euro(s)')
else:
    print(heur,'heure(s) au tarif horaire de 1.0 euro(s)')

    if hdeb < 7 or hfin >= 17:
        print(heur, 'heure(s) au tarif horaire de 2.0 euro(s)')
    else:
        print(heur, 'heure(s) au tarif horaire de 1.0 euro(s)')

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
