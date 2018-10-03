rep = 3
liste = []
while rep>=0:
    rep = int(input("Entrez des nombres (<0 pour terminer la liste"))
    if rep >= 0:
        liste.append(rep)
print("La liste est saisie")
moyenne = 0
for i in range(0,len(liste)):
    moyenne += int(liste[i])
moyenne = moyenne/len(liste)

print(moyenne)
