fail1 = open("sisseränne.txt", encoding="UTF-8")
fail2 = open("väljaränne.txt", encoding="UTF-8")
sisse = []
välja = []
for rida in fail1:
        sisse.append(int(rida))
for rida in fail2:
        välja.append(int(rida))
fail1.close()
fail2.close()
saldo = []
for i in range(10):
    arv=sisse[i]-välja[i]
    saldo.append(arv)
print(saldo)
jrk = 0
if max(saldo) > 0:
    for i in range(10):
        jrk += 1
        if max(saldo) == saldo[i]:
            break
    print("Suurim positiivne rändesaldo oli " + str(jrk) + ". aastal.")
else:
    print("Positiivse rändesaldoga aastaid ei ole.")