def kuu_nimi(jrk):
    jrk -= 1
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuud[jrk]
def kuupäev_sõnena(form):
    x = form.split(".")
    jrk = int(x[1])
    kuu = kuu_nimi(jrk)
    return x[0] + ". " + kuu + " " + x[2] + ". a"
a = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
print(kuupäev_sõnena(a))
