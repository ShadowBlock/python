arv = int(input("Siestage täisarv: "))
arv1 = arv
nisu = 1
while arv > 1:
    nisu *= 2
    arv -= 1
print("Nisuteri " + str(arv1) + ". ruudu eest: " + str(nisu))