from random import *
kokku = 14
summa = int()
arv = int(input("Mitu pöialpoissi tahab õunu? "))
while arv > 0:
    õun = randint(1,2)
    print(õun)
    summa += õun
    arv -= 1
kokku -= summa
print("Lumivalgekesele jäi " + str(kokku))