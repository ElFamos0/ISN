# -*- coding: utf-8 -*
note = float(input("Quel est votre note au bac ?"))
if note <10 :
    print("Vous allez aux rattrapages, bon courage !")
elif note >= 10 and note<12 :
    print("Vous n'avez pas de mention")
elif note >=12 and note<14 :
    print("Vous avez la mention assez bien ! Bravo !")
elif note >=14 and note<16:
    print("Vous avez la mention bien ! Félicitation !")
else :
    print("Vous avez la mention très bien ! Excellent !")