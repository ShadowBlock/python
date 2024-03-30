l = 0
n = 0
loendaja = 0
while loendaja <= 4:
    if oige[l] == kasutaja_sona[n]:
        a = colored(kasutaja_sona[n], "green")
        varvitud.insert(n, a)
        l += 1
        n += 1
        loendaja += 1
    else:
        a = colored(kasutaja_sona[n], "grey")
        varvitud.insert(n, a)
        l += 1
        n += 1
        loendaja += 1
        
l = 0
n = 0
loendaja = 0
while loendaja <= 4:
    if n == 5:
        n = 0
        l += 1
        loendaja += 1
    else:
        if oige[l] == kasutaja_sona[n]:
            a = colored(kasutaja_sona[n], "yellow")
            varvitud.insert(n, a)
            n += 1
        else:
            a = colored(kasutaja_sona[n], "grey")
            varvitud.insert(n, a)
            n += 1

oige = faili_sonad[suvaline_arv]