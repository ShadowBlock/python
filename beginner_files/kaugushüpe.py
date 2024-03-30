def parandatud_tulemus(viganeTulemus, mõõteparandus):
    tegelikTulemus = viganeTulemus + mõõteparandus / 100
    return tegelikTulemus

faili_nimi = input("Sisestage failinimi: ")
parandus = float(input("Sisestage parandus sentimeetrites: "))
normatiiv = float(input("Sisestage meistrivõistluste normatiiv meetrites: "))

fail = open(faili_nimi, encoding="UTF-8")

normatiiv_taitnud = 0
n_taitnud = []
kokku = 0
normatiiv_taitnud = 0

print("Tegelikud tulemused")
for rida in fail:
    c = round(parandatud_tulemus(float(rida), parandus), 2)
    print(str(c))
    if c >= normatiiv:
        normatiiv_taitnud +=1
        kokku += c

keskmine = kokku / normatiiv_taitnud

print("Normatiivi täitis " + str(normatiiv_taitnud) + ".")
if arv > 0:
    print("Täitnute keskmine on " + str(round(keskmine, 2)) + ".")