# -*- coding: utf-8 -*-
'''
	Auteur : Malo
	Programme : Scrabble Eco+ Edition
	Enonce : On place dans une chaine 7 lettres correspondant au tirage du jeu d'un joueur au Scrabble. Réaliser un programme qui
	demande au joueur un mot et lui dit si il peut en effet le former avec ses 7 lettres.
'''
'''
1 point : E *15, A *9, I *8, N *6, O *6, R *6, S *6, T *6, U *6, L *5
2 points : D *3, M *3, G *2
3 points : B *2, C *2, P *2
4 points : F *2, H *2, V *2
8 points : J *1, Q *1
10 points : K *1, W *1, X *1, Y *1, Z *1
Pour un total de 100 jetons
'''
from random import randint
#voici les lettres d'un scrabble selon les règles française
a = "AAAAAAAAABBCCDDDEEEEEEEEEEEEEEEFFGGHHIIIIIIIIJKLLLLLMMMNNNNNNOOOOOOPPQRRRRRRSSSSSSTTTTTTUUUUUUVVWXYZ"
Scrabble = list(a)
lettreschoisies = []

for i in range(0,7):#pour choisir 7 lettres au hasard
	b = randint(0,len(a)-1)
	lettreschoisies += a[b]

print("Voici votre tirage : ",lettreschoisies)

rep = input("Quel mot pouvez vous former avec ces lettres ? : ").upper()
print(rep)
rep = list(rep)
win = True #déclaration des variables utiles pour plus tard
compteur = 0
for j in range (0,len(rep)):#boucle qui permet de comparer ce qu'à entrer l'utilisateur avec les lettres choisies
    lettrestrouvees = str(lettreschoisies).find(rep[j])
    if lettrestrouvees < 0 :
        print("Vous ne pouvez pas former ce mot")
        win = False
        break
    else: #lorsque une lettre est en une fois on l'enlève (remplacé par un +)
        if str(lettreschoisies).count(rep[j]) == 1:
            lettreschoisies = str(lettreschoisies).replace(rep[j],"+")
        else: #lorsque une lettre est en plusieurs exemplaires on fait un compteur
        # car sinon on remplace complètement la lettre au lieu d'en supprimer un seul exemplaire
            Lettre_en_plusieurs_fois = str(lettreschoisies).count(rep[j])
            if compteur >= Lettre_en_plusieurs_fois:
                print("Vous ne pouvez pas former ce mot")
                win = False
                break
            else :
                compteur += 1

if win == True:     #fin du programme
    print("Bien jouée !")

