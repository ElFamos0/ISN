#coding: utf-8
phrase = "Ce mot est le plus long : Oskar"
a = phrase.split(" ")
comparateur = 0
for i in range(0,len(a)):
    if len(a[i])>comparateur:
        best = ''
        comparateur=len(a[i])
        best = a[i]
    else:
        pass
print("Le mot le plus long",best)