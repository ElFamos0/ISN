# -*- coding : utf8 -*-
a = int(input("a : "))
b = int(input("b : "))
c = a
d = b

while c != d:
    if c > d:
        c = c-d
    elif c < d:
        d = d-c

print("Le pgcd de",a,"et",b,"est",c)