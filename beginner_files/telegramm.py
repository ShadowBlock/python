failinimi = input("Sisestage failinimi: ")
f = open(failinimi, encoding="UTF-8")
failisisu = f.read().upper()
asendatud = failisisu.replace("Ä","AE")
asendatud = asendatud.replace("Ü","UE")
asendatud = asendatud.replace("Ö","OE")
asendatud = asendatud.replace("Õ","OE")
print(asendatud)

f.close()