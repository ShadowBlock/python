fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:

    vastuvõetud.append(int(rida))

fail.close()
arv = int(input("Palun sisestage, millise aasta andmed vajate: "))
aasta = arv
arv -= 2011
print(str(aasta) + ". aastal oli vastuvõetuid " + str(vastuvõetud[arv]))