ring = int(input("Sisesta ringide arv: "))
porgand = 0
loendaja = 0
jrk = 1
while ring > 0:
    loendaja += 1
    if (loendaja%2) == 0:
        porgand = porgand + 2 * jrk
        jrk += 1
        ring -= 1
    else:
        ring -= 1
print("Porgandite koguarv on " + str(porgand) + ".")