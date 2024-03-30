def mahlapakkide_arv(kg):
    arv = round(float(kg * 0.4/3))
    return arv
kg = float(input("Sisesta õunte kogus kilogrammides: "))
print(mahlapakkide_arv(kg))