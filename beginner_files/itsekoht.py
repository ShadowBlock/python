from random import *
valik = str(input("Kas soovite istekohta ise valida (ise) või loosida (loosida)? "))
if valik == "loos":
    loos = randint(1,3)
    if loos == 1:
        print("Istekoht loositi. Aknakoht")
    else:
        print("Istekoht loositi. Vahekäigukoht")
else:
    asukoht = str(input("Kas soovite istuda akna ääres (aken) või mitte (muu)? "))
    if asukoht == "aken":
        print("Valisite ise. Aknakoht")
    else:
        print("Valisite ise. Vahekäigukoht")