def eelarve(arv):
    return 10*arv+55
failinimi = input("Sisesta failinimi: ")
f = open(failinimi, encoding="UTF-8")

jah = 0
mdea = 0

for rida in f:
    osalised = rida.split()
    for vastus in osalised:
        if vastus == "+":
            jah += 1
        if vastus == "?":
            mdea += 1

kokku = jah + mdea

print("Kutsutud on " + str(kokku) + " inimest")
print(str(jah) + " inimest tuleb")
print("Maksimaalne eelarve: " + str(eelarve(kokku)) + " EUR")
print("Minimaalne eelarve: " + str(eelarve(jah)) + " EUR")