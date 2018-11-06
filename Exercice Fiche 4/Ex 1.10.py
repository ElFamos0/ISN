# -*- coding: utf-8 -*

def nombreoccurences(x,m):
	"Indique le nombre de fois ou une lettre x est présente dans un str m"
	a = m.count(x)
	return a
m = input("Phrase : ")
x = input("Lettre dans la phrase")

print("il y a",nombreoccurences(x,m),"fois la lettre",x,"dans",m)
help(nombreoccurences)