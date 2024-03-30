def juurdekasv(pindala, kasv):
    arv = pindala * 0.4047 * kasv
    return round(arv, 2)

fail = input("Sisesta failinimi: ")
kasvud = float(input("Sisesta aastane juurdekasv hektari kohta tihumeetrites: "))
piir = float(input("Sisesta piir, mitmest aakrist suuremad metsatükid arvesse võetakse: "))

f = open(fail, encoding="UTF-8")
p = []
loendaja = 0
for rida in f:
    p.append(float(rida))
f.close()
for el in p:
    if el > piir:
        print("Metsatüki aastane juurdekasv on " + str(juurdekasv(el, kasvud)))
        loendaja += 1
    else:
        print("Metsatükki ei võeta arvesse")
print("Arvutati " + str(loendaja) + " metsatüki juurdekasv.")