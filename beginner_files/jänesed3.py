ring = int(input("Sisesta ringide arv: "))
porgand = 0
jrk = 1
for loendaja in range(1, ring, 2):
    porgand += 2*jrk
    jrk += 1
print(porgand)