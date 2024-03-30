vanus = int(input("Sisestage enda vanus: "))
sugu = str(input("Sisestage enda sugu: "))
treening = int(input("Sisestage treeningu tüüp: "))
if treening == 1:
    if sugu == "m" or sugu == "M":
        max = (220 - vanus)*0.70
        min = (220 - vanus)*0.50
        print("Pulsisagedus peaks olema vahemikus " + str(round(min)) + " kuni " + str(round(max)) + ".")
    elif sugu == "n" or sugu == "N":
        max = (206 - vanus*0.88)*0.70
        min = (206 - vanus*0.88)*0.50
        print("Pulsisagedus peaks olema vahemikus " + str(round(min)) + " kuni " + str(round(max)) + ".")
    else:
        print("Sellist sugu ei eksisteeri.")
if treening == 2:
    if sugu == "m" or sugu == "M":
        max = (220 - vanus)*0.80
        min = (220 - vanus)*0.70
        print("Pulsisagedus peaks olema vahemikus " + str(round(min)) + " kuni " + str(round(max)) + ".")
    elif sugu == "n" or sugu == "N":
        max = (206 - vanus*0.88)*0.80
        min = (206 - vanus*0.88)*0.70
        print("Pulsisagedus peaks olema vahemikus " + str(round(min)) + " kuni " + str(round(max)) + ".")
    else:
        print("Sellist sugu ei eksisteeri.")
if treening == 3:
    if sugu == "m" or sugu == "M":
        max = (220 - vanus)*0.87
        min = (220 - vanus)*0.80
        print("Pulsisagedus peaks olema vahemikus " + str(round(min)) + " kuni " + str(round(max)) + ".")
    elif sugu == "n" or sugu == "N":
        max = (206 - vanus*0.88)*0.87
        min = (206 - vanus*0.88)*0.80
        print("Pulsisagedus peaks olema vahemikus " + str(round(min)) + " kuni " + str(round(max)) + ".")
    else:
        print("Sellist sugu ei eksisteeri.")
else:
    print("Sellist treeningtüüpi ei eksisteeri.")