def eelarve(arv):
    return 10*arv+55
maks = int(input("Mitu inimest on kutsutud? "))
minim = int(input("Mitu inimest tuleb? "))
print("Maksimaalne eelarve: " + str(eelarve(maks)))
print("Minimaalne eelarve: " + str(eelarve(minim)))