ring = int(input("Sisesta ringide arv: "))
porgand = 0
jrk = 1
lisada = 0
while ring > 0:
    lisada = lisada + jrk
    porgand += lisada
    jrk += 1
    ring -= 1
print("Porgandite koguarv on " + str(porgand) + ".")