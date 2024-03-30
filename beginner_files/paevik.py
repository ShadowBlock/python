from datetime import datetime
kuupäev_kellaaeg = datetime.today()
sissekanne = input("Sisesta sissekande tekst: ")
f = open("paevik.txt", "a", encoding="UTF-8")
f.write("\n\n" + str(kuupäev_kellaaeg) + "\n" + sissekanne)
f.close()