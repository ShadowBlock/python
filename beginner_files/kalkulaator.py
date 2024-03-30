from easygui import *
esimene = integerbox("Sisestage esimene täisarv lõigus 1-10", lowerbound = 1, upperbound = 10)
teine = integerbox("Sisestage teine täisarv lõigus 1-10", lowerbound = 1, upperbound = 10)
nupud = ["+","-","*"]
mark = buttonbox("Valige tehe:", choices = nupud)
if mark == "+":
    arv = esimene + teine
elif mark == "-":
    arv = esimene - teine
elif mark == "*":
    arv = esimene * teine
msgbox("Tehte tulemus on " + str(arv) + ".")