punktid = float(input("Palun sisesta punktisumma: "))
if punktid > 100.0:
    print("Vigane punktisumma")
elif punktid >= 85.0:
    print("Vastuvõtt tagatud")
elif punktid >= 66.0:
    print("Kandideerimine vastuvõtule")
elif punktid >= 0.0:
    print("Vähem kui kandideerimiseks vajalik")
else:
    print("Vigane punktisumma")