def banner(a):
    return a.upper()
korda = int(input("Mitu korda soovite reklaamlauset kuvada? "))
a = input("Sisestage reklaamlause: ")
while korda > 0:
    print(banner(a))
    korda -= 1