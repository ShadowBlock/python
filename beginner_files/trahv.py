nimi = str(input("Sisestage oma nimi: "))
lkiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tkiirus = int(input("Sisestage tegelik kiirus (km/h): "))
trahv = min(190, (tkiirus - lkiirus) * 4)
print(nimi + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot.")