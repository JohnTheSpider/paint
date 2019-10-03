from tkinter import *





canvas_wight = 500
canvas_height = 500
brush_size = 10
color = "black"

def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1,y1,x2,y2,fill=color,outline=color)



root = Tk()
root.title("Недо Paint")
#root.minsize(700,700)
#root.geometry("700x700")
w = Canvas(root, width=canvas_wight,height=canvas_height,bg="white")
#w.scale(700, 700)
w.bind("<B1-Motion>", paint)
w.grid(row=2, column=0,
       columnspan=7,padx=5,pady=5, sticky=E+W+S+N)
w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)

plus_btn = Button(text="+", width=2, command=lambda: changesizeplus())
minus_btn = Button(text="-", width=2, command=lambda: changesizeminus())
red_btn = Button(text="Красный", width=8, command=lambda: changecolor("red"))
blue_btn = Button(text="Синий", width=8, command=lambda: changecolor("blue"))
gray_btn = Button(text="Серый", width=8, command=lambda: changecolor("gray"))
white_btn = Button(text="Белый", width=8, command=lambda: changecolor("white"))
green_btn = Button(text="Зеленый", width=8, command=lambda: changecolor("green"))
pink_btn = Button(text="Розовый", width=8, command=lambda: changecolor("pink"))
black_btn = Button(text="Черный", width=8, command=lambda: changecolor("black"))
orange_btn = Button(text="Оранжевый", width=8, command=lambda: changecolor("orange"))
yellow_btn = Button(text="Желтый", width=8, command=lambda: changecolor("yellow"))
brown_btn = Button(text="Коричневый", width=10, command=lambda: changecolor("brown"))

red_btn.grid(row=0,column=0)
blue_btn.grid(row=0,column=1)
gray_btn.grid(row=0,column=2)
white_btn.grid(row=0,column=3)
green_btn.grid(row=0,column=4)
pink_btn.grid(row=1,column=0)
black_btn.grid(row=1,column=1)
orange_btn.grid(row=1,column=2)
yellow_btn.grid(row=1,column=3)
brown_btn.grid(row=1,column=4)
plus_btn.grid(row=0,column=5)
minus_btn.grid(row=1,column=5)
def changecolor(new_color):
    global color
    color = new_color
def changesizeplus():

    global brush_size
    brush_size += 1;

def changesizeminus():
   global brush_size
   if brush_size > 0:

    brush_size -= 1;

print(root)
root.mainloop()
