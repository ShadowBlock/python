inimesed = int(input("Inimeste arv: "))
kohad = int(input("Kohtade arv: "))
bussid = inimesed // kohad
if inimesed % kohad != 0:
    bussid += 1
viimane = inimesed - kohad * (bussid - 1)
print("Busse vaja: " + str(bussid))
print("Viimases bussis inimesi: " + str(viimane))