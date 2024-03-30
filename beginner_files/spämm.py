suurus = float(input("Sisestage kirja suurus: "))
pealkiri = str(input("Sisestage kirja teema pealkiri: "))
fail = str(input("Kas kirjaga on kaasas fail?: ")).lower()
if suurus > 1 and fail == "jah" or pealkiri == "":
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")