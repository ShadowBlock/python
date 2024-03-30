punktid = int(input("Sisesta punktide arv: "))
 
if punktid >= 90:
    print("Hinne A")
elif punktid >= 80:
    print("Hinne B")
elif punktid >= 70:
    print("Hinne C")
elif punktid >= 60:
    print("Hinne D")
elif punktid > 50:
    print("Hinne E")
elif punktid == 50:
    print("Hinne E, oled osav raisk...")
else:
    print("Hinne F, ole targem...")