from tkinter import *


jojo = "hh"
root = Tk()
root.title("Разрешение")
canvas_wight = root.winfo_screenwidth()
print(canvas_wight)
canvas_wight /= 2
canvas_height = root.winfo_screenheight()
print(canvas_height)
canvas_height /= 2
print(canvas_wight)
print(canvas_height)
w = Canvas(root, width=canvas_wight,height=canvas_height,bg="white")
message = StringVar()
message1 = StringVar()
field_w = Entry( width=25, textvariable=message)
field_h = Entry( width=25, textvariable=message1)
def standart():


    root.destroy()
defolt_btn = Button(text="По умолчанию (1/2 экрана)", width=25, command=lambda:standart())
def maximum():
    global jojo
    jojo = "gg"
    root.destroy()
full_btn = Button(text="Полный экран", width=25, command=lambda: maximum())
wb = Button(text="Ширина окна", width=10, command=lambda: changesizeplus())
hb = Button(text="Высота окна", width=10, command=lambda: changesizeplus())
w.grid(row=2, column=0,
       columnspan=7,padx=5,pady=5, sticky=E+W+S+N)
go_btn = Button(root, text="Вперед!", width=25, command=root.destroy)
w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)
field_h.grid(row=0,column=1)
go_btn.grid(row=2,column=1)
hb.grid(row=0,column=2)
wb.grid(row=1,column=2)
field_w.grid(row=1,column=1)
defolt_btn.grid(row=0,column=0)
full_btn.grid(row=1,column=0)
root.mainloop()
gg = 0
gg1 = 0

if message.get() != "":
 gg = int(re.search(r'\d+', message.get()).group(0))
 print(gg)
if message1.get() != "":
 gg1 = int(re.search(r'\d+', message1.get()).group(0))
 print(gg1)





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

if message1.get() == "":
 if jojo != "hh":
  canvas_wight = root.winfo_screenwidth()
if message.get() == "":
    if jojo != "hh":
        canvas_height = root.winfo_screenheight()
if gg1 != 0:
    canvas_height = gg1
if gg != 0:
    canvas_wight = gg

print(jojo)
print(canvas_height)
print(canvas_wight)
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
purple_btn = Button(text="Фиолетовый", width=10, command=lambda: changecolor("purple"))
golub_btn = Button(text="Зеленый", width=10, command=lambda: changecolor("lime"))

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
plus_btn.grid(row=0,column=6)
minus_btn.grid(row=1,column=6)
purple_btn.grid(row=0,column=5)
golub_btn.grid(row=1,column=5)

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
