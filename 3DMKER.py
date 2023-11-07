#📔
from tkinter import *
from tkinter import Entry
import tkinter as tk
from PIL import Image, ImageTk,ImageGrab
import math
import os
#fin📔
#val
i = 0
xc , yc = 0, 0
x=y=swch=0
swch = 1
fig= []
custom = []
numefig = ""
cust = []
#finval
#inter🙂
#🪟
root = tk.Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.config(bg="blue")
canvas =tk.Canvas(root,bg="white",height=(80/100*root.winfo_screenheight()),width=(70/100*root.winfo_screenwidth()),borderwidth=1,relief="solid")
btnlogo = Canvas(root, width=7/100*root.winfo_screenwidth(), height=(10/100*root.winfo_screenheight())*2, bg="white")
#fin🪟#functii🤖
#🗺️
def cords(event = None):
    global xc,yc
    xc ,yc = event.x ,event.y
    canvas.bind("<Motion>", local)
def local(event):
    global xc , yc
    xc , yc = event.x, event.y
    root.title(f"x={xc} y={yc}")
def push(event):
    global xc , yc,cust,fig
    cust.append(xc)
    cust.append(yc)
    if int(len(cust)) >= 6 :
        fig = canvas.create_polygon(cust,fill= str(inp_bgclr.get()),outline=str(inp_borderclr.get()),width=int(inp_brdgrosime.get()))
        cust.clear()
    print(cust)
def clearfunc(event):
    print("")
def pushd(event):
    global xc , yc,cust,fig
    cust.append(xc)
    cust.append(yc)
    if len(cust) == 6:
        cust.append(cust[0])
        cust.append(cust[1])
    if len(cust) == 10:
        cust.append(cust[2])
        cust.append(cust[3])
        fig = canvas.create_polygon(cust,fill= str(inp_bgclr.get()),outline=str(inp_borderclr.get()),width=int(inp_brdgrosime.get()))
        cust.clear()
    if len(cust) == 12:
        cust.clear()
    print(cust)
   
#fin🗺️
#figuri
def crpatrat():
    global fig, numefig , x1, y1,configuratii,fig,sigur,x,y
    numefig = ""
    fig = 0
    x,y=0,0
    configuratii = int(inp_lungimeA.get())
    x1 = int(inp_lungimeA.get())
    y1 = int(inp_lungimeA.get())
    numefig = "patrat"
    fig = canvas.create_rectangle(x,y,x1,y1,fill= str(inp_bgclr.get()),outline=str(inp_borderclr.get()),width=int(inp_brdgrosime.get()))
def crdreptunghi():
    global fig, numefig,x,y,x1,y1,configuratiia,configuratiib
    x,y = 0,0
    configuratiia = int(inp_lungimeA.get())
    configuratiib = int(inp_lungimeB.get())
    x1 = int(inp_lungimeA.get())
    y1 = int(inp_lungimeB.get())
    fig = canvas.create_rectangle(x,y,x1,y1,fill= str(inp_bgclr.get()),outline=str(inp_borderclr.get()),width=int(inp_brdgrosime.get()))
    numefig = "dreptunghi"
def crcerc():
    global fig, numefig,x,y,x1,y1,configuratiia,configuratiib
    x,y = 0,0
    configuratiia = int(inp_lungimeA.get())
    configuratiib = int(inp_lungimeB.get())
    x1 = int(inp_lungimeA.get())
    y1 = int(inp_lungimeB.get())
    fig = canvas.create_oval(x,y,x1,y1,fill= str(inp_bgclr.get()),outline=str(inp_borderclr.get()),width=int(inp_brdgrosime.get()))
    numefig = "cerc"
def crtriunghi():
    global numefig, swch
    numefig = "triunghi"
    swch += 1
    if (swch%2) == 0:
     canvas.bind("<Button-1>",push)
    elif (swch%2) == 1:
     canvas.bind("<Button-1>",clearfunc)
def crromb():
    global numefig, swch,fig,x1,y1,x2,y2,x3,y3,x4,y4,configuratiia,configuratiib
    numefig = "romb"
    configuratiia = int(inp_lungimeA.get())
    configuratiib = int(inp_lungimeB.get())
    x1,y1,x2,y2,x3,y3,x4,y4 =0,int(inp_lungimeB.get())/2,int(inp_lungimeA.get())/2,0,int(inp_lungimeA.get()),int(inp_lungimeB.get())/2,int(inp_lungimeA.get())/2,int(inp_lungimeB.get())
    fig = canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,fill=str(inp_bgclr.get()),outline=str(inp_borderclr.get()),width=inp_brdgrosime.get())
def crcub():
    global fig,numefig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,a,b,c
    a = int(inp_lungimeA.get())
    b = int(inp_lungimeB.get())
    c = int(inp_lungimeC.get()) 
    numefig= "cub"
    x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12=0,c,b,c,b,a+c,0,a+c,0,c,c,0,b+c,0,c+b,a,b,a+c,b,c,c+b,0,b,c
    fig =canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,fill=inp_bgclr.get(),outline=inp_borderclr.get(),width=int(inp_brdgrosime.get()))
def croctogon():
    global numefig, swch,fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,a
    numefig = "octogon"
    a = int(inp_lungimeA.get())
    x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8 = 0,a,a,0,a*2,0,3*a,a,a*3,a*2,a*2,a*3,a,a*3,0,a*2
    fig= canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,fill=str(inp_bgclr.get()),outline=str(inp_borderclr.get()),width=int(inp_brdgrosime.get())) 
def crparalelogram():
    global numefig, swch,fig,x1,y1,x2,y2,x3,y3,x4,y4,b,c,a
    numefig = "paralelogram"   
    a = int(inp_lungimeA.get())
    b = int(inp_lungimeB.get())
    c = int(inp_lungimeC.get())
    x1,y1,x2,y2,x3,y3,x4,y4 = c, 0,c+a ,0,a,b,0,b 
    fig = canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,fill=str(inp_bgclr.get()),outline=str(inp_borderclr.get()),width=int(inp_brdgrosime.get()))
def crpiramida():
    global numefig, swch
    numefig = "piramida"
    swch += 1
    if (swch%2) == 0:
     canvas.bind("<Button-1>",pushd)
    elif (swch%2) == 1:
     canvas.bind("<Button-1>",clearfunc)
def crhexa():
    global numefig, swch,fig,a,b,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6 
    numefig = "hexagon"
    a = int(inp_lungimeA.get())
    b = int(inp_lungimeB.get())
    x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6 =0,a,b,0,a+b,0,b+a+b,a,b+a,a*2,b,a*2
    fig= canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,fill=str(inp_bgclr.get()),outline=str(inp_borderclr.get()),width=int(inp_brdgrosime.get())) 
def crcreion():
    global numefig, swch,da
    numefig = "custom"
    swch += 1
    if (swch%2) == 0:
     root.bind("<Button-1>", clr(True)) 
    elif (swch%2) == 0:
     root.bind("<Button-1>",clr(False))
#
def clr(event):
    global xc , yc,cust,fig,mihai,da
    da = True
    clrd()
def stopit(event):
    global da
    da = False
def clrd():
    global da,xc ,yc
    if da:
     canvas.create_oval(xc -int(inp_lungimeA.get())/2,yc -int(inp_lungimeA.get())/2, xc,yc,fill=str(inp_bgclr.get()),outline=str(inp_borderclr.get()),width=int(inp_brdgrosime.get()))
     root.after(1,clrd)
def dlt():
    global fig
    canvas.delete(fig)
def dltall():
    global fig
    canvas.delete("all")
def mrrm():
    obj = canvas.find_all()
    for obj in obj:
        canvas.itemconfig(obj, fill = "white",outline="gray")
def custommode():
    global custom
    custom.append(inp_customx.get())
    custom.append(inp_customy.get())
    if inp_customx.get() == "exit":
        custom.clear()
    canvas.create_polygon(custom,fill=inp_bgclr.get(),width=int(inp_brdgrosime.get()),outline=inp_borderclr.get())
def screanshot():
    global i
    i+=1 
    x1 = canvas.winfo_rootx()
    y1 = canvas.winfo_rooty()
    x2 = x1 +canvas.winfo_width()
    y2 = y1 + canvas.winfo_height()
    dirnm , filenm =os.path.split(os.path.abspath(__file__))

    scrnsht = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    if(os.path.isdir(f"{str(dirnm)}/{str(inp_numefolder.get())}")):
        scrnsht.save(f"{str(dirnm)}/{str(inp_numefolder.get())}/{str(i)}.png")
    else:
        os.mkdir(f"{str(dirnm)}/{str(inp_numefolder.get())}")
        scrnsht.save(f"{str(dirnm)}/{str(inp_numefolder.get())}/{str(i)}.png") 
#finfiguri
#functiimiscare
def verif(event):
    global fig,numefig,xc,yc,da,x,y,x1,y1,x2,y2,x3,y3,x4,y4
    if str(numefig) == "patrat":
        if (x <= xc <=x1) & (y<= yc<= y1):
            da = True
            mvpatrat()
    elif str(numefig) == "dreptunghi":
        if (x <= xc <=x1) & (y<= yc<= y1):
            da = True
            mvdreptunghi()
    elif str(numefig) == "cerc":
        if (x <= xc <=x1) & (y<= yc<= y1):
            da = True
            mvcerc()
    elif numefig == "romb":
        global configuratiia,configuratiib
        if (x1 <= xc <= x3) &(y2<= yc <= y4):
            da= True
            mvromb()
    elif numefig == "cub":
        global x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,a,b,c
        if (x1 <= xc <= x2)&(y2<= yc<=y4):
            da= True
            mvcub()
    elif numefig == "octogon":
        if (x1<= xc <= x4)&(y2 <= yc <= y6):
            da = True
            mvoctogon()
    elif numefig == "paralelogram":
        if (x4 <= xc <= x2) &(y1 <= yc <=y4):
            da = True
            mvparalelogram()
    elif numefig == "hexagon":
        if (x1 <=xc <= x4)&(y2 <= yc <=y6):
            da =True
            mvhexagon()
def mvpatrat():
    global xc,yc,x,y,x1,y1,fig,da,configuratii
    if da:
        x = xc - configuratii/2
        y = yc - configuratii/2
        x1 = xc + configuratii/2
        y1 = yc + configuratii/2
        canvas.coords(fig,x,y,x1,y1)
        root.after(1,mvpatrat)   
def mvdreptunghi():
    global xc,yc,x,y,x1,y1,fig,da,configuratiia,configuratiib
    if da:
        x = xc - configuratiia/2
        y = yc - configuratiib/2
        x1 = xc + configuratiia/2
        y1 = yc + configuratiib/2
        canvas.coords(fig,x,y,x1,y1)
        root.after(1,mvdreptunghi)     
def mvcerc():
    global xc,yc,x,y,x1,y1,fig,da,configuratiia,configuratiib
    if da:
        x = xc - configuratiia/2
        y = yc - configuratiib/2
        x1 = xc + configuratiia/2
        y1 = yc + configuratiib/2
        canvas.coords(fig,x,y,x1,y1)
        root.after(1,mvcerc)   
def mvromb():
    global x1,y1,x2,y2,x3,y3,x4,y4,configuratiia,configuratiib
    if da:
        x1 = xc - configuratiia/2
        y1 = yc
        x2 = xc
        y2 = yc - configuratiib/2
        x3 = xc + configuratiia/2
        y3 = yc
        x4 = xc
        y4 = yc + configuratiib/2
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4)
        root.after(1,mvromb)
def mvcub():
    global fig,numefig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,a,b,c
    if da:
        x1 = xc - b/2
        y1 = yc - a/2
        x2 = xc + b/2
        y2 = yc - a/2
        x3 = xc + b/2
        y3 = yc + a/2
        x4 = xc - b/2
        y4 = yc + a/2
        x5 = xc - b/2
        y5 = yc - a/2
        x6 = x5 + c
        y6 = y5 - c
        x7 = x6 + b
        y7 = y5 - c
        x8 = xc + b/2
        y8 = yc - a/2
        x9 = xc + b/2
        y9 = yc + a/2
        x10 = (xc + b/2) + c
        y10 = (yc + a/2) -c
        x11 = x2 + c
        y11 = y2 - c
        x12 = xc + b/2
        y12 = yc - a/2
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12) 
        root.after(1,mvcub)
#❗R.I.P❗
def mvoctogon():
    global numefig, swch,fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,a
    if da:
        x1 = xc - 1.5 * a
        y1 = yc - 0.5 * a
        x2 = xc - 0.5 * a
        y2 = yc - 1.5 * a
        x3 = xc + 0.5 * a
        y3 = yc - 1.5 * a
        x4 = xc + 1.5 * a
        y4 = yc - 0.5 * a
        x5 = xc - 1.5 * a
        y5 = yc + 0.5 * a
        x2 = xc + 0.5 * a
        y2 = yc + 1.5 * a
        x3 = xc - 0.5 * a
        y3 = yc + 1.5 * a
        x4 = xc + 1.5 * a
        y4 = yc + 0.5 * a
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8) 
        root.after(1,mvoctogon)
    """❗Repara coordonatele"""      
def mvparalelogram():
    global fig,x1,y1,x2,y2,x3,y3,x4,y4,a,b,c
    if da:
        x4 = xc - a/2
        y4 = yc + b/2
        x3 = xc + a/2
        y3 = yc + b/2
        x2 = xc + a/2 + c
        y2 = yc - b/2
        x1 = xc - (a/2 - c)
        y1 = yc - b/2
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4)
        root.after(1,mvparalelogram)
def mvhexagon():
    global x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,a,b,c,fig
    if da:
        x1 = xc-(a/2 + b)
        y1 = yc 
        x2 = xc - a/2
        y2 = yc - a
        x3 = xc + a/2 
        y3= yc - a
        x4 = xc + (a/2 + b)
        y4 = yc
        x5 = xc + a/2
        y5 = yc + a
        x6 = xc - a/2
        y6 = yc + a
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
        root.after(1,mvhexagon)

#   x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6 =0,a,b,0,a+b,0,b+a+b,a,a+b,a+b,b,b+b+a,0,a+b
def dreapta():
    global fig,numefig,xc,yc,da,x,y,x1,y1,x2,y2,x3,y3,x4,y4,a
    if str(numefig) == "patrat":
         da = True
         dreaptada()
    elif str(numefig) == "dreptunghi":
         da = True
         dreaptada()
    elif str(numefig) == "cerc":
         da = True
         dreaptada()
    elif numefig == "romb":
        global configuratiia,configuratiib
        da = True
        dreaptaromb()
    elif numefig == "cub":
        global x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,a,b,c
        da= True
        dreaptacub()
    elif numefig == "octogon":
        da = True
        dreaptaoctogon()
    elif numefig == "paralelogram":
        da = True
        dreaptaparalelogram()
    elif numefig == "hexagon":
        da =True
        dreaptahexagon()
def dreaptada():
    global fig,x,y,x1,y1,da
    if da:
        x +=1
        x1+=1
        canvas.coords(fig,x,y,x1,y1)
        root.after(10,dreaptada)
def dreaptaromb():
    global fig,x1,y1,x2,y2,x3,y3,x4,y4,da
    if da:
        x1 += 1
        x2 += 1
        x3 += 1
        x4 += 1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4)
        root.after(10,dreaptaromb)
def dreaptacub():
    global fig,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x1,y1,x2,y2,x3,y3,x4,y4,da
    if da:
        x1 += 1
        x2 += 1
        x3 += 1
        x4 += 1
        x5 += 1
        x6 += 1
        x7 += 1
        x8 += 1
        x9 += 1
        x10+= 1
        x11+= 1
        x12+= 1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12)
        root.after(10,dreaptacub)
def dreaptaoctogon():
    global fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,da
    if da:
     x1 += 1
     x2 += 1
     x3 += 1
     x4 += 1
     x5 += 1
     x6 += 1
     x7 += 1
     x8 += 1
     canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8)
     root.after(10,dreaptaoctogon)
def dreaptaparalelogram():
    global fig,x1,y1,x2,y2,x3,y3,x4,y4,a,b,c
    if da:
        x4 += 1
        x3 += 1
        x2 += 1
        x1 += 1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4)
        root.after(10,dreaptaparalelogram)
def dreaptahexagon():
    global x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,a,b,c,fig
    if da:
        x1 += 1
        x2 += 1
        x3 += 1
        x4 += 1
        x5 += 1
        x6 += 1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
        root.after(10,dreaptahexagon)
def stanga():
    global fig,numefig,xc,yc,da,x,y,x1,y1,x2,y2,x3,y3,x4,y4,a
    if str(numefig) == "patrat":
         da = True
         stangada()
    elif str(numefig) == "dreptunghi":
         da = True
         stangada()
    elif str(numefig) == "cerc":
         da = True
         stangada()
    elif numefig == "romb":
        global configuratiia,configuratiib
        da = True
        stangaromb()
    elif numefig == "cub":
        global x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,a,b,c
        da= True
        stangacub()
    elif numefig == "octogon":
        da = True
        stangaoctogon()
    elif numefig == "paralelogram":
        da = True
        stangaparalelogram()
    elif numefig == "hexagon":
        da =True
        stangahexagon()
def stangada():
    global fig,x,y,x1,y1,da
    if da:
        x =x -1
        x1=x1-1
        canvas.coords(fig,x,y,x1,y1)
        root.after(10,stangada)
def stangaromb():
    global fig,x1,y1,x2,y2,x3,y3,x4,y4,da
    if da:
        x1 =x1 - 1
        x2 =x2- 1
        x3 = x3-1
        x4 = x4-1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4)
        root.after(10,stangaromb)
def stangacub():
    global fig,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x1,y1,x2,y2,x3,y3,x4,y4,da
    if da:
        x1 = x1- 1
        x2 = x2 - 1
        x3 = x3-1
        x4 = x4-1
        x5 = x5-1
        x6 = x6-1
        x7 = x7-1
        x8 = x8-1
        x9 = x9-1
        x10= x10-1
        x11= x11-1
        x12= x12-1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12)
        root.after(10,stangacub)
def stangaoctogon():
    global fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,da
    if da:
     x1 = x1-1
     x2 = x2-1
     x3 = x3 -1
     x4 = x4 -1
     x5 = x5 -1
     x6 = x6 -1
     x7 = x7 -1
     x8 = x8 -1
     canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8)
     root.after(10,stangaoctogon)
def stangaparalelogram():
    global fig,x1,y1,x2,y2,x3,y3,x4,y4,a,b,c
    if da:
        x4 =x4 - 1
        x3 =x3- 1
        x2 =x2- 1
        x1 =x1- 1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4)
        root.after(10,stangaparalelogram)
def stangahexagon():
    global x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,a,b,c,fig
    if da:
        x1 =x1-1
        x2 =x2-1
        x3 =x3-1
        x4 =x4-1
        x5 =x5-1
        x6 = x6-1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
        root.after(10,stangahexagon)
def jos():
    global fig,numefig,xc,yc,da,x,y,x1,y1,x2,y2,x3,y3,x4,y4,a
    if str(numefig) == "patrat":
         da = True
         josda()
    elif str(numefig) == "dreptunghi":
         da = True
         josda()
    elif str(numefig) == "cerc":
         da = True
         josda()
    elif numefig == "romb":
        global configuratiia,configuratiib
        da = True
        josromb()
    elif numefig == "cub":
        global x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,a,b,c
        da= True
        joscub()
    elif numefig == "octogon":
        da = True
        josoctogon()
    elif numefig == "paralelogram":
        da = True
        josparalelogram()
    elif numefig == "hexagon":
        da =True
        joshexagon()
def josda():
    global fig,x,y,x1,y1,da
    if da:
        y +=1
        y1+=1
        canvas.coords(fig,x,y,x1,y1)
        root.after(10,josda)
def josromb():
    global fig,x1,y1,x2,y2,x3,y3,x4,y4,da
    if da:
        y1 += 1
        y2 += 1
        y3 += 1
        y4 += 1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4)
        root.after(10,josromb)
def joscub():
    global fig,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x1,y1,x2,y2,x3,y3,x4,y4,da
    if da:
        y1 += 1
        y2 += 1
        y3 += 1
        y4 += 1
        y5 += 1
        y6 += 1
        y7 += 1
        y8 += 1
        y9 += 1
        y10+= 1
        y11+= 1
        y12+= 1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12)
        root.after(10,joscub)
def josoctogon():
    global fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,da
    if da:
     y1 += 1
     y2 += 1
     y3 += 1
     y4 += 1
     y5 += 1
     y6 += 1
     y7 += 1
     y8 += 1
     canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8)
     root.after(10,josoctogon)
def josparalelogram():
    global fig,x1,y1,x2,y2,x3,y3,x4,y4,a,b,c
    if da:
        y4 += 1
        y3 += 1
        y2 += 1
        y1 += 1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4)
        root.after(10,josparalelogram)
def joshexagon():
    global x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,a,b,c,fig
    if da:
        y1 += 1
        y2 += 1
        y3 += 1
        y4 += 1
        y5 += 1
        y6 += 1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
        root.after(10,dreaptahexagon)
def sus():
    global fig,numefig,xc,yc,da,x,y,x1,y1,x2,y2,x3,y3,x4,y4,a
    if str(numefig) == "patrat":
         da = True
         susda()
    elif str(numefig) == "dreptunghi":
         da = True
         susda()
    elif str(numefig) == "cerc":
         da = True
         susda()
    elif numefig == "romb":
        global configuratiia,configuratiib
        da = True
        susromb()
    elif numefig == "cub":
        global x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,a,b,c
        da= True
        suscub()
    elif numefig == "octogon":
        da = True
        susoctogon()
    elif numefig == "paralelogram":
        da = True
        susparalelogram()
    elif numefig == "hexagon":
        da =True
        sushexagon()
def susda():
    global fig,x,y,x1,y1,da
    if da:
        y =y-1
        y1=y1-1
        canvas.coords(fig,x,y,x1,y1)
        root.after(10,susda)
def susromb():
    global fig,x1,y1,x2,y2,x3,y3,x4,y4,da
    if da:
        y1 =y1 - 1
        y2 =y2- 1
        y3 = y3-1
        y4 = y4-1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4)
        root.after(10,susromb)
def suscub():
    global fig,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x1,y1,x2,y2,x3,y3,x4,y4,da
    if da:
        y1 = y1- 1
        y2 = y2 - 1
        y3 = y3-1
        y4 = y4-1
        y5 = y5-1
        y6 = y6-1
        y7 = y7-1
        y8 = y8-1
        y9 = y9-1
        y10= y10-1
        y11= y11-1
        y12= y12-1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12)
        root.after(10,suscub)
def susoctogon():
    global fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,da
    if da:
     y1 = y1-1
     y2 = y2-1
     y3 = y3 -1
     y4 = y4 -1
     y5 = y5 -1
     y6 = y6 -1
     y7 = y7 -1
     y8 = y8 -1
     canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8)
     root.after(10,susoctogon)
def susparalelogram():
    global fig,x1,y1,x2,y2,x3,y3,x4,y4,a,b,c
    if da:
        y4 =y4 - 1
        y3 =y3- 1
        y2 =y2- 1
        y1 =y1- 1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4)
        root.after(10,susparalelogram)
def sushexagon():
    global x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,a,b,c,fig
    if da:
        y1 =y1-1
        y2 =y2-1
        y3 =y3-1
        y4 =y4-1
        y5 =y5-1
        y6 =y6-1
        canvas.coords(fig,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
        root.after(10,sushexagon)
#finfunctiimiscare
#finfunctii🤖#activfunctii
canvas.bind("<FocusIn>",cords)
root.bind("<Button-3>",stopit)
root.bind("<Button-1>",verif)
canvas.focus_set()
#finactivfunctii
#🔘
#📷
gunoi = PhotoImage(file = r"logo/trash-can.png")
gunoim = gunoi.subsample(10,10)
patratic = PhotoImage(file = r"logo/square.png")
patraticm = patratic.subsample(7,7)
dreptunghiic =PhotoImage(file = r"logo/rectangular-shape-outline.png")
dreptunghiicm = dreptunghiic.subsample(5,5)
triunghiic =PhotoImage(file = r"logo/triangle.png")
trinughiicm = triunghiic.subsample(10,10)
rombic =PhotoImage(file = r"logo/rhombus.png")
rombicm = rombic.subsample(10,10)
octogonic =PhotoImage(file = r"logo/octagon.png")
octogonicm = octogonic.subsample(11,11)
cercic =PhotoImage(file = r"logo/dry-clean.png")
cercicm = cercic.subsample(6,6)
paralelogramic =PhotoImage(file = r"logo/parallelogram.png")
paralelogramicm = paralelogramic.subsample(9,9)
piramidaic = PhotoImage(file = r"logo/pyramid.png")
piramidaicm = piramidaic.subsample(10,10)
cubic = PhotoImage(file= r"logo/cube.png")
cubicm = cubic.subsample(10,10)
hexagonic =PhotoImage(file= r"logo/hexagon-geometrical-shape-outline.png")
hexagonicm = hexagonic.subsample(10,10)
mopic =PhotoImage(file= r"logo/mop.png")
mopicm = mopic.subsample(10,10)
customic = PhotoImage(file = r"logo/inclined-pencil.png")
customicm = customic.subsample(10,10)
captureic = PhotoImage(file = r"logo/camera.png")
captureicm = captureic.subsample(10,10)
fantic = PhotoImage(file = r"logo/ghost.png")
fanticm = fantic.subsample(10,10)
cstmic = PhotoImage(file = r"logo/hammer.png")
cstmicm = cstmic.subsample(10,10)
stangaic = PhotoImage(file = r"logo/arrow.png")
stangaicm = stangaic.subsample(10,10)
susic = PhotoImage(file = r"logo/up-arrow.png")
susicm = susic.subsample(10,10)
josic = PhotoImage(file = r"logo/down-arrow.png")
josicm = josic.subsample(10,10)
dreaptaic = PhotoImage(file = r"logo/right-arrow.png")
dreaptaicm = dreaptaic.subsample(10,10)
#fin📷
btn_patrat=tk.Button(root,relief="solid",borderwidth=1,bg="white",activebackground="lightblue",command=crpatrat,image=patraticm).place(x=0,y=0,width=int(7/100*root.winfo_screenwidth())/2,height=(int(10/100*root.winfo_screenheight())/2))
btn_cerc=tk.Button(root,relief="solid",borderwidth=1,bg="white",activebackground="lightblue",command=crcerc,image=cercicm).place(x=int(7/100*root.winfo_screenwidth())/2,y=0,width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
btn_dreptunghi=tk.Button(root,relief="solid",borderwidth=1,bg="white",activebackground="lightblue",command=crdreptunghi,image=dreptunghiicm).place(x=int(7/100*root.winfo_screenwidth()),y=0,width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
btn_triunghi=tk.Button(root,relief="solid",borderwidth=1,bg="white",activebackground="lightblue",command=crtriunghi,image=trinughiicm).place(x=int(7/100*root.winfo_screenwidth())*1.5,y=0,width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
btn_romb=tk.Button(root,relief="solid",borderwidth=1,bg="white",activebackground="lightblue",command=crromb,image=rombicm).place(x=0,y=int(10/100*root.winfo_screenheight())/2,width=int(7/100*root.winfo_screenwidth())/2,height=int(10/100*root.winfo_screenheight())/2)
btn_octogon=tk.Button(root,relief="solid",borderwidth=1,bg="white",activebackground="lightblue",command=croctogon,image=octogonicm).place(x=int(7/100*root.winfo_screenwidth())/2,y=int(10/100*root.winfo_screenheight())/2,width=int(7/100*root.winfo_screenwidth())/2,height=int(10/100*root.winfo_screenheight())/2)
btn_paralelogram=tk.Button(root,relief="solid",activebackground="lightblue",borderwidth=1,bg="white",command=crparalelogram,image=paralelogramicm).place(x=int(7/100*root.winfo_screenwidth()),y=int(10/100*root.winfo_screenheight())/2,width=int(7/100*root.winfo_screenwidth())/2,height=int(10/100*root.winfo_screenheight())/2)
btn_piramida=tk.Button(root,image=piramidaicm,relief="solid",activebackground="lightblue",borderwidth=1,bg="white",command=crpiramida).place(x=int(7/100*root.winfo_screenwidth())*1.5,y=int(10/100*root.winfo_screenheight())/2,width=int(7/100*root.winfo_screenwidth())/2,height=int(10/100*root.winfo_screenheight())/2)
btn_cub=tk.Button(root,image=cubicm,relief="solid",activebackground="lightblue",borderwidth=1,bg="white",command=crcub,).place(x=0,y=int(10/100*root.winfo_screenheight()),width=int(7/100*root.winfo_screenwidth())/2,height=(int(10/100*root.winfo_screenheight())/2))
btn_hexa=tk.Button(root,image=hexagonicm,relief="solid",activebackground="lightblue",borderwidth=1,bg="white",command=crhexa).place(x=int(7/100*root.winfo_screenwidth())/2,y=int(10/100*root.winfo_screenheight()),width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
btn_mop=tk.Button(root,image=mopicm,relief="solid",activebackground="lightblue",borderwidth=1,bg="white",command=dltall).place(x=int(7/100*root.winfo_screenwidth()),y=int(10/100*root.winfo_screenheight()),width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
btn_custom=tk.Button(root,image=cstmicm,relief="solid",activebackground="lightblue",borderwidth=1,bg="white",command=custommode).place(x=int(7/100*root.winfo_screenwidth())*1.5,y=int(10/100*root.winfo_screenheight()),width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
btn_creion=tk.Button(root,image=customicm,relief="solid",activebackground="lightblue",borderwidth=1,bg="white",command=crcreion).place(x = 0,y=int(10/100*root.winfo_screenheight())*1.5,width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
btn_dlt=tk.Button(root,borderwidth=1,relief="solid",bg="white",activebackground="lightblue",image=gunoim,compound=LEFT,command=dlt).place(x = int(7/100*root.winfo_screenwidth())/2,y=int(10/100*root.winfo_screenheight())*1.5,width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
btn_capture=tk.Button(root,image=captureicm,relief="solid",borderwidth=1,activebackground="lightblue",bg="white",command=screanshot).place(x = int(7/100*root.winfo_screenwidth()),y=int(10/100*root.winfo_screenheight())*1.5,width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
btn_fant=tk.Button(root,image=fanticm,relief="solid",borderwidth=1,activebackground="lightblue",bg="white",command=mrrm).place(x = int(7/100*root.winfo_screenwidth())*1.5,y=int(10/100*root.winfo_screenheight())*1.5,width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
btn_stanga=tk.Button(root,image=stangaicm,relief="solid",activebackground="lightblue",borderwidth=1,bg="white",command=stanga).place(x = 0,y=int(10/100*root.winfo_screenheight())*2,width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
btn_sus=tk.Button(root,borderwidth=1,relief="solid",bg="white",activebackground="lightblue",image=susicm,command=sus).place(x = int(7/100*root.winfo_screenwidth())/2,y=int(10/100*root.winfo_screenheight())*2,width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
btn_jos=tk.Button(root,image=josicm,relief="solid",borderwidth=1,activebackground="lightblue",bg="white",command=jos).place(x = int(7/100*root.winfo_screenwidth()),y=int(10/100*root.winfo_screenheight())*2,width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
btn_dreapta=tk.Button(root,image=dreaptaicm,relief="solid",borderwidth=1,activebackground="lightblue",bg="white",command=dreapta).place(x = int(7/100*root.winfo_screenwidth())*1.5,y=int(10/100*root.winfo_screenheight())*2,width=int(7/100*root.winfo_screenwidth())/2,height=int((10/100*root.winfo_screenheight()))/2)
#fin🔘
#🚮
inf_lungimeA = tk.Label(root,text="lungimeA=",borderwidth=1,bg="blue",fg="white",font=True).place(x=int(85/100*root.winfo_screenwidth()),height=(int(10/100*root.winfo_screenheight())/4))
inf_lungimeB = tk.Label(root,text="lungimeB=",borderwidth=1,bg="blue",fg="white",font=True).place(x=int(85/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4),height=(int(10/100*root.winfo_screenheight())/4))
inf_lungimeC = tk.Label(root,text="lungimeC=",borderwidth=1,bg="blue",fg="white",font=True).place(x=int(85/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*2,height=(int(10/100*root.winfo_screenheight())/4))
inf_bgclr = tk.Label(root,text="culoare=",borderwidth=1,bg="blue",fg="white",font=True).place(x=int(85/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*3,height=(int(10/100*root.winfo_screenheight())/4))
inf_borderclr = tk.Label(root,text="culoareBRD=",borderwidth=1,bg="blue",fg="white",font=True).place(x=int(85/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*4,height=(int(10/100*root.winfo_screenheight())/4))
inf_brdgrosime = tk.Label(root,text="grosimeBRD=",borderwidth=1,bg="blue",fg="white",font=True).place(x=int(85/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*5,height=(int(10/100*root.winfo_screenheight())/4))
inf_unghi1 = tk.Label(root,text="unghi1=",borderwidth=1,bg="blue",fg="white",font=True).place(x=int(85/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*6,height=(int(10/100*root.winfo_screenheight())/4))
inf_unghi2 = tk.Label(root,text="unghi2=",borderwidth=1,bg="blue",fg="white",font=True).place(x=int(85/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*7,height=(int(10/100*root.winfo_screenheight())/4))
inf_numefolder = tk.Label(root,text="nume=",borderwidth=1,bg="blue",fg="white",font=True).place(x=int(85/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*8,height=(int(10/100*root.winfo_screenheight())/4))
da = tk.Label(root,text="----------CUSTOM----------",borderwidth=1,bg="blue",fg="white",font=True).place(x=int(85/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*9,height=(int(10/100*root.winfo_screenheight())/4))
inf_customx = tk.Label(root,text="x=",borderwidth=1,bg="blue",fg="white",font=True).place(x=int(85/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*10,height=(int(10/100*root.winfo_screenheight())/4))
inf_customy = tk.Label(root,text="y=",borderwidth=1,bg="blue",fg="white",font=True).place(x=int(85/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*11,height=(int(10/100*root.winfo_screenheight())/4))
inp_lungimeA = tk.Entry(root,borderwidth=1)
inp_lungimeA.place(x=int(91/100*root.winfo_screenwidth()),height=(int(10/100*root.winfo_screenheight())/4),width=6/100*root.winfo_screenwidth())
inp_lungimeB = tk.Entry(root,borderwidth=1)
inp_lungimeB.place(x=int(91/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4),height=(int(10/100*root.winfo_screenheight())/4),width=6/100*root.winfo_screenwidth())
inp_lungimeC = tk.Entry(root,borderwidth=1)
inp_lungimeC.place(x=int(91/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*2,height=(int(10/100*root.winfo_screenheight())/4),width=6/100*root.winfo_screenwidth())
inp_bgclr = tk.Entry(root,borderwidth=1)
inp_bgclr.place(x=int(91/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*3,height=(int(10/100*root.winfo_screenheight())/4),width=6/100*root.winfo_screenwidth())
inp_borderclr = tk.Entry(root,borderwidth=1)
inp_borderclr.place(x=int(91/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*4,height=(int(10/100*root.winfo_screenheight())/4),width=6/100*root.winfo_screenwidth())
inp_brdgrosime = tk.Entry(root,borderwidth=1)
inp_brdgrosime.place(x=int(91/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*5,height=(int(10/100*root.winfo_screenheight())/4),width=6/100*root.winfo_screenwidth())
inp_unghi1 = tk.Entry(root,borderwidth=1)
inp_unghi1.place(x=int(91/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*6,height=(int(10/100*root.winfo_screenheight())/4),width=6/100*root.winfo_screenwidth())
inp_unghi2 = tk.Entry(root,borderwidth=1)
inp_unghi2.place(x=int(91/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*7,height=(int(10/100*root.winfo_screenheight())/4),width=6/100*root.winfo_screenwidth())
inp_numefolder = tk.Entry(root,borderwidth=1)
inp_numefolder.place(x=int(91/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*8,height=(int(10/100*root.winfo_screenheight())/4),width=6/100*root.winfo_screenwidth())
inp_customx = tk.Entry(root,borderwidth=1,relief="solid")
inp_customx.place(x=int(87/100*root.winfo_screenwidth()),y=(int(10/100*root.winfo_screenheight())/4)*10,height=(int(10/100*root.winfo_screenheight())/4),width=6/100*root.winfo_screenwidth())
inp_customy = tk.Entry(root,borderwidth=1,relief="solid")
inp_customy.place(x=int(87/100*root.winfo_screenwidth()),y=int(10/100*root.winfo_screenheight())/4*11,height=int(10/100*root.winfo_screenheight())/4,width=6/100*root.winfo_screenwidth())
add_cords_button = tk.Button(root,borderwidth=2,text="=>",bg="lightblue",command=custommode)
add_cords_button.place(x=int((87/100*root.winfo_screenwidth())+(6/100*root.winfo_screenwidth())),y=(int(10/100*root.winfo_screenheight())/4)*10,height=(int(10/100*root.winfo_screenheight())/4)*2,width=6/100*root.winfo_screenwidth()/5)
#fin🚮
#fin_inter🙂
#endexec
canvas.pack()
root.mainloop()
#endexec
