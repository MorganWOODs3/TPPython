BASE=4
fromage=float (800.0)
eau=float (2)
ail=float(2)
pain=float(400)

nbConvives= int(input('Entrez le nombre de personne(s) conviées à la fondue:'))

nvqA=(fromage*nbConvives)/BASE
nvqB=(eau*nbConvives)/BASE
nvqC=(ail*nbConvives)/BASE
nvqD=(pain*nbConvives)/BASE


print('Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut:')
print('-',nvqA,'gramme de fromage')
print('-',nvqB,'de Litre d"eau')
print('-',nvqC,'d"ail')
print('-',nvqD,'gramme de pain')