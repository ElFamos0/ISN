# -*- coding: utf-8 -*

h = int(input("Heure 1 : "))  # entrée des deux horaires
m = int(input("Minute 1 : "))
s = int(input("Seconde 1 : "))
h2 = int(input("Heure 2 : "))
m2 = int(input("Minute 2: "))
s2 = int(input("Seconde 2: "))


def conversionheure(h, m, s):
    h = 3600 * h
    m = 60 * m
    return(h + m + s)


def différencedetemps(o, i):
    "Calcul une différence de temps entre deux horaires"
    diff_sec = abs(o - i)  # nous avons un résultat en seconde que l'on doit transformer en heures minutes secondes
    heure = diff_sec / 3600
    diff_sec %= 3600  # modulo pour rajouter les secondes qui rentrent pas en minutes ou en heures
    minute = diff_sec / 60
    diff_sec %= 60
    return("Différence de temps : " + str(int(heure)) + " h  " + str(int(minute)) + " min  " + str(int(diff_sec)) + " sec  ")


print(différencedetemps(conversionheure(h, m, s), conversionheure(h2, m2, s2)))  # appel des fonctions
