# -*- coding : utf8 -*-
liste1 = "AGWPSGGASAGLAIL"
liste2 = "IGWPSAGASAGLWIL"
hamming = 0
for i in range(0,len(liste1)):
    if liste1[i] == liste2[i]:
        pass
    else:
        hamming += 1

print(hamming)