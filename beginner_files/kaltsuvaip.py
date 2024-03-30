def lõimede_pikkus(pikkus, arv):
    õige_pikkus = round(arv * (pikkus * 1.2 + 0.5), 2)
    return õige_pikkus
    
faili_nimi = input("Sisestage failinimi: ")
pikk = int(input("Sisestage 5-meetriste ja pikemate vaipade lõimede arv: "))
lühike = int(input("Sisestage lühemate vaipade lõimede arv: "))

fail = open(faili_nimi, encoding="UTF-8")

summa = 0

for rida in fail:
    if float(rida) >= 5:
        c = lõimede_pikkus(float(rida), pikk)
        print(c)
        summa += c
    else:
        c = lõimede_pikkus(float(rida), lühike)
        print(c)
        summa += c
        
print("Kõigi vaipade peale läheb vaja " + str(summa) + " meetrit lõimeniiti.")