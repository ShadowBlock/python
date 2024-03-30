fail = open("ostud.txt", encoding="UTF-8")
ostud = []
for rida in fail:
    ostud.append(rida)
fail.close()
print(ostud)