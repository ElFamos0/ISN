phrase = input("Rentre une phrase : ")
phrase_inverse = ""

for lettre in phrase:
    phrase_inverse = lettre + phrase_inverse
print(phrase_inverse)