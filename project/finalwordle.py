#Töö autorid on Stiven Lille ja Juhan Puusepp

#Worlde mängukirjeldus

#Wordle mäng valib ühe suvalise 5-tähelise sõna, mida ta kasutajale ei avalda alguses
#Kasutajal on 6 võimalust see sõna ära arvata, iga katse järel programm näitab, kui lähedal on kasutaja sõna äraarvamisele
#Kasutaja peab pakkuma suvalise 5-tähelise sõna.
#Kui kasutajal on täht või tähed õiged, aga vales kohas, siis need muutuvad kollaseks.
#Kui kasutajal on täht või tähed õiged ja õiges kohas, siis need muutuvad roheliseks.
#Kui kasutajal ei ole tähed õiged, jäävad tähed tavaliseks mustaks.
#Kui kasutaja pakub õige sõna, lähevad kõik tähed roheliseks ning programm edastab võiduteatise.

#Programmi töökäik

#Alguses loeb failist kõik sõnad.
#Seejärel valib suvaliselt 1 sõna.
#Seejärel jaotab programm selle sõna järjendiks.
#Kasutajal lastakse pakkuda üks sõna.
#Programm muudab kasutaja pakutud sõna järjendiks.
#Programm kontrollib tähtede õigsust.
#Programm käitub nii iga pakutud sõna puhul.
#Iga katse puhul väljastab programm värvitud versiooni pakutud sõnast.
#Õige sõna korral väljastab programm võiduteatise.
#Vale sõna korral, kui on katsed läbi, väljastab programm kaotuseteatise.
#Programm laseb nii kaotuse kui ka võidu korral mängu uuesti alustada.

from random import randint
import sys
from termcolor import colored, cprint
from easygui import *
import webbrowser

#Failist suvalise sõna valimine

#Avab faili "100sona.txt" ning muudab selle järjendiks
#Valib suvalise numbri 0-99 ning leiab sellele vastava sõna

f = open("100sona.txt", encoding="UTF-8")
faili_sonad = []
suvaline_arv = randint(0, 99)
for rida in f:
    faili_sonad.append(rida)
f.close()

oige = faili_sonad[suvaline_arv]

#Lisab uue muutuja, mis loeb õigesti arvatud tähtede arvu
voit = 0

#Sõna küsimine ja selle kontroll

#Küsib kasutajalt viietähelise sõna
#Programm eeldab, et sisestatud on alati viietäheline sõna
#Programm tekitab muutujaid sõnade kontrollimiseks
#Esialgu kontrollib, kas sõnas on "rohelisi" tähti
#Järgmisena kontrollib, kas sõnas on "kollaseid" tähti
#Kui on "kollased" tähed, siis kontrollib, et kas ta äkki ikka on hoopis "roheline"
#Kui ei vasta mitte millelegi, siis jätab tähe mustaks
#Kordab seda while-tsükliga 4 korda veel, et kontrolliks kõik tähed
#Lõpuks väljastab kontrollitud sõna kasutajale

def kontroll():
    kasutaja_sona = input("Sisesta viietäheline sõna: ")

    varvitud = []
    
    global voit
    l = 0
    n = 0
    tahed = 0
    lisakontroll = 0
    while tahed < 5:
        while l < 5:
            if l == n and oige[l] == kasutaja_sona[n]:
                c = colored(kasutaja_sona[n], "green")
                varvitud.insert(n, c)
                voit +=1
                break
            elif oige[l] == kasutaja_sona[n]:
                c = colored(kasutaja_sona[n], "yellow")
                varvitud.insert(n, c)
                l = 0
                while lisakontroll < 5:
                    if l == n and oige[l] == kasutaja_sona[n]:
                        c = colored(kasutaja_sona[n], "green")
                        varvitud.insert(n, c)
                        voit +=1
                        break
                    lisakontroll += 1
                    l += 1
                break
            l += 1
            if l == 5:
                varvitud.insert(n, kasutaja_sona[n])
        tahed +=1
        n += 1
        l = 0
        lisakontroll = 0
    print(varvitud[0], varvitud[1], varvitud[2], varvitud[3], varvitud[4])

#Roundide kontroll

#Võtab global muutujujad, et kontrollida, kas katsete arv on läbi
#Kui katsete arv on läbi, siis viskab ette EasyGUI kasti, kus on võimalik uuesti alustada mängu või õppida sõnu sonaveeb.ee-st
#Sellisel juhul valib uue sõna ja resetib muutujad
#Kui katsete arv ei ole läbi ja õige sõna ei ole veel arvatud, siis annab kasutajal uuesti proovida
#Kui õige sõna on leitud, siis viskab ette EasyGUI kasti, kus on võimalik uuesti alustada mängu
def roundid():
    global korda
    global voit
    global suvaline_arv
    global oige
    while korda > 0:
        if voit == 5:
            nupud2 = ["Alusta uuesti"]
            vajutati2 = buttonbox("Leidsid õige sõna! Oled võitnud!", choices = nupud2)
            if vajutati2 == "Alusta uuesti":
                voit = 0
                korda = 6
                suvaline_arv = randint(0, 99)
                oige = faili_sonad[suvaline_arv]
                kontroll()
                roundid()
                break
            break
        elif voit < 5:
            korda -= 1
            if korda == 0:
                nupud3 = ["Proovi uuesti", "Õpi eesti keele sõnavara"]
                vajutati3 = buttonbox("Su katsete arv sai kahjuks otsa. Oled luuser!", choices = nupud3)
                if vajutati3 == "Proovi uuesti":
                    voit = 0
                    korda = 6
                    suvaline_arv = randint(0, 99)
                    oige = faili_sonad[suvaline_arv]
                    kontroll()
                    roundid()
                    break
                if vajutati3 == "Õpi eesti keele sõnavara":
                    webbrowser.open('http://sonaveeb.ee')
                    break
            print("Sul on alles " + str(korda) + " katset.")
            voit = 0
            kontroll()

#Mängu alustus

#Tekitab muutuja, millega seadistab kordade arvu
#Valib pildi "näidis.png", et seda tuua EasyGUI messageboxi
#Loetleb ette mängu reeglid ja annab võimaluse mängu alustada

korda = 6

nupud = ["Alusta!"]
img = "naidis.png"
vajutati = buttonbox("Tere tulemast Stiveni ja Juhani eestikeelsesse Wordle sõnamängu!\nMängu kirjeldus:\nprogramm valib ühe suvalise 5-tähelise sõna ning kasutajal on 6 võimalust seda õigesti pakkuda.\nKui kasutajal on täht või tähed õiged, aga vales kohas, siis vastavad tähed muutuvad kollaseks.\nKui kasutajal on täht või tähed õiged ja õiges kohas, siis need muutuvad roheliseks.\nKui kasutajal ei ole tähed õiged, jäävad tähed tavaliseks mustaks.\nKui kasutaja pakub õige sõna, lähevad kõik tähed roheliseks ning edastab võiduteatise.", image = img, choices = nupud)
if vajutati == "Alusta!":
    kontroll()
    roundid()
