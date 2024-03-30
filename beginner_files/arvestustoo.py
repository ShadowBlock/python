import math

def kartulite_kogus(suurus):
    kogus = suurus * 27 / 100
    return kogus

faili_nimi = input("Sisesta faili nimi: ")

fail = open(faili_nimi, encoding="UTF-8")

jrk = 0
kokku = 0

for rida in fail:
    rida = rida.strip()
    a = kartulite_kogus(float(rida))
    if float(rida) >= 600:
        jrk += 1
        print(str(jrk) + ". põld: see ei ole kartulipõld")
    else:
        jrk += 1
        print(str(jrk) + ". põld: suurus " + str(rida) + ", kartuleid vaja " + str(a) + " kg")
        kokku += round(a, 1)

fail.close()

print("Kartuleid läheb vaja " + str(kokku) + " kg")

kotid = kokku / 20
print("Osta tuleb " + str(math.ceil(kotid)) + " kotti seemnekartuleid")