# -*- coding : utf8 -*-

prix = eval(input("Entrer le prix de base de l'article (en euro): "))
nwprix = prix

nbrdereduc = eval(input("Combien d'augmentation/ diminution en 1,x ou 0,x : "))
reducs = []
for i in range(0,nbrdereduc):
	reducs.append(eval(input("Entrer les aug/dim dans l'ordre d'enchainement. :")))

for x in range(0,len(reducs)):
	nwprix = nwprix*reducs[x]

print(round(nwprix,2),"€")

if nwprix > prix:
	print("Augmentation de :",round(nwprix-prix,2),"€")
elif nwprix < prix:
	print("Réduction de : ",round(prix-nwprix,2),"€")
else:
	print("Le prix ne change pas")