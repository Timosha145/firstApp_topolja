from tkinter import *
k=0
def clicker(event):
	global k
	k+=1
	button1.config(text=k)
def clicker1(event):
	global k
	k-=1
	button1.config(text=k)
def txt_to_lbl(event):
	text=txt.get()
	lbl.configure(text=text)
	txt.delete(0,END)
def choose():
	choosy=var.get()
	lbl.configure(text=choosy)
window=Tk()
window.title("AbobusAmogus")
window.geometry("500x800")
button1=Button(window,text="Aboba",font="Arial 20",width=20,fg="blue",bg="yellow",relief=RAISED)
button1.pack()
button1.bind("<Button-1>",clicker)
button1.bind("<Button-3>",clicker1)
lbl=Label(window,text="ABoba",font="Arial 30",height=3,width=20, fg="blue",bg="yellow",relief="solid")
lbl.pack()
txt=Entry(window,fg="blue",bg="pink",justify=CENTER)
txt.pack()
txt.bind("<Return>",txt_to_lbl)
i1=PhotoImage(file="1.png")
i2=PhotoImage(file="2.png")
i3=PhotoImage(file="3.gif")
var=StringVar()
var.set("one")
r1=Radiobutton(window,image=i1,variable=var,value="one",command=choose())
r2=Radiobutton(window,image=i2,variable=var,value="two",command=choose())
r3=Radiobutton(window,image=i3,variable=var,value="three",command=choose())
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
window.mainloop()
