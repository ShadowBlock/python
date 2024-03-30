from tkinter import *
 
raam = Tk()
raam.title("Liiklusmärk nr. 751")
tahvel = Canvas(raam, width=450, height=650)

## Ümarate nurkadega ristküliku kood on võetud siit: https://stackoverflow.com/questions/44099594/how-to-make-a-tkinter-canvas-rectangle-with-rounded-corners
def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return tahvel.create_polygon(points, **kwargs, smooth=True)

#Tagataust liilusmärgile
tahvel.create_rectangle(0, 0, 450, 650, fill="#398cc6", outline="#398cc6")
ääred = round_rectangle(5, 5, 447, 647, radius=50, fill="#398cc6", outline="#ffffff", width=8)
tahvel.create_rectangle(30, 70, 420, 430, fill="#ffffff", outline="#ffffff")

#Staadion

ring1 = round_rectangle(55, 200, 395, 410, radius=200, fill="black")
ring2 = round_rectangle(80, 225, 370, 385, radius=150, fill="white")
ring3 = round_rectangle(90, 235, 360, 375, radius=130, fill="black")
ring4 = round_rectangle(110, 255, 340, 355, radius=100, fill="#ffffff")

#Lipud
i = 0
while i < 3:
    tahvel.create_rectangle(150+i*80, 90, 155+i*80, 190, fill="black", outline="black")
    tahvel.create_rectangle(110+i*80, 92, 150+i*80, 132, fill="black", outline="black")
    i += 1

tahvel.pack()
raam.mainloop()