import random
summa = 0
while summa < 100:
    juhuslik = random.randint(1, 6)
    summa += juhuslik
print(juhuslik)
if juhuslik == 1:
    print("Juh")
else:
    print("Putsi")