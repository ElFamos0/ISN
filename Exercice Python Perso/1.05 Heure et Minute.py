# -*- coding : utf8 -*-
#Code Parfaitement fonctionnel
heures = int(input("Entrer les heures : "))
minutes = int(input("Entrer les minutes : "))

if heures < 23:
    if minutes < 59:
        minutes += 1
        if minutes < 10:
            minutes = "0"+str(minutes)
    elif minutes == 59:
        minutes = "00"
        heures += 1
        if heures < 10:
            heures = "0"+str(heures)
else :
    if minutes < 59:
        minutes+=1
    elif minutes ==59:
        heures = "00"
        minutes = "00"
print("Il sera", heures,"h",minutes,"dans 1 minute")