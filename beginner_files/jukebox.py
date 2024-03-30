failinimi = str(input("Sisesta failinimi: "))
fail = open(failinimi, encoding="UTF-8")

jrk = 1
muusika = []
print("Muusikapalade valik:")
for rida in fail:
        print(str(jrk) + ". " + rida)
        muusika.append(str(rida))
        jrk +=1
fail.close()
valik = int(input("Vali muusikapala number: "))
valik -= 1
print("Mängitav muusikapala on " + muusika[valik])