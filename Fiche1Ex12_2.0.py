from random import*

mot = input("entrer un mot")
mot2 = mot

for j in range (len(mot)):
    i = randint(j,len(mot)-1)
    if i==j:
        a = mot2[j]
        b = mot2[i]
        mot2 = mot2[0:j]+b+mot2[j+1:i]+a+mot2[i+1:]

print(mot2)
