def tablettide_arv(f):
    c = (f - 32) * 5/9
    if c > 38:
        return 2
    else:
        return 0

faili_nimi = input("Sisestage failinimi: ")

fail = open(faili_nimi, encoding="UTF-8")

kraadid = []

for rida in fail:
    kraadid.append(float(rida))
fail.close()

print(kraadid)

karp = float(input("Mitu tabletti on karbis: "))

summa = 0

for i in range(0, len(kraadid)-1):
    summa += tablettide_arv(kraadid[i])

karpide_arv = summa / karp

print("Kokku kulus " + str(summa) + " tabletti, mis on " + str(round(karpide_arv, 1)) + " karpi.")