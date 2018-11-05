# -*- coding : utf8 -*-

print("Combien de notes souhaitez vous entrer : ")
a = int(input())
notes = 0
for i in range(a):
	note = int(input("Note : "))
	notes += note

moyenne = round((notes/a),2)
print("La moyenne est de : ",moyenne)





