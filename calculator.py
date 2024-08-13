from tkinter import *

def bclick(number):
    global val
    val=val+str(number)
    data.set(val)
def bclear():
    global val
    val=""
    data.set("")
    
def bEquals():
    global val
    result=str(eval(val))
    data.set(result)

win=Tk()
win.title("Mycalculator")
win.geometry("320x380")

val=''
data=StringVar()
win.resizable(width="False",height="False")


e1=Entry(win,textvariable=data,font=("arial",20),bd=15,bg="grey",justify="right",width=19)
e1.grid(row=0,columnspan=4)

bcross=Button(win,text="x",font=("arial",20,"bold"),bd=5,fg="red",bg="powderblue",width=4,command=bclear)
bcross.place(x=0,y=80)
bdot=Button(win,text=".",font=("arial",20,"bold"),bd=5,fg="red",bg="powderblue",width=4,command=lambda:bclick('.'))
bdot.place(x=80,y=80)
bpt=Button(win,text="%",font=("arial",20,"bold"),bd=5,fg="red",bg="powderblue",width=4,command=lambda:bclick('%'))
bpt.place(x=160,y=80)
bslash=Button(win,text="/",font=("arial",20,"bold"),bd=5,fg="red",bg="powderblue",width=4,command=lambda:bclick('/'))
bslash.place(x=240,y=80)
b7=Button(win,text="7",font=("arial",20,"bold"),bd=5,width=4,bg="powderblue",command=lambda:bclick(7))
b7.place(x=0,y=140)
b8=Button(win,text="8",font=("arial",20,"bold"),bd=5,width=4,bg="powderblue",command=lambda:bclick(8))
b8.place(x=80,y=140)
b9=Button(win,text="9",font=("arial",20,"bold"),bd=5,width=4,bg="powderblue",command=lambda:bclick(9))
b9.place(x=160,y=140)
bmul=Button(win,text="*",font=("arial",20,"bold"),bd=5,fg="red",bg="powderblue",width=4,command=lambda:bclick('*'))
bmul.place(x=240,y=140)
b4=Button(win,text="4",font=("arial",20,"bold"),bd=5,width=4,bg="powderblue",command=lambda:bclick(4))
b4.place(x=0,y=200)
b5=Button(win,text="5",font=("arial",20,"bold"),bd=5,width=4,bg="powderblue",command=lambda:bclick(5))
b5.place(x=80,y=200)
b6=Button(win,text="6",font=("arial",20,"bold"),bd=5,width=4,bg="powderblue",command=lambda:bclick(6))
b6.place(x=160,y=200)
bsub=Button(win,text="-",font=("arial",20,"bold"),bd=5,fg="red",bg="powderblue",width=4,command=lambda:bclick('-'))
bsub.place(x=240,y=200)
b1=Button(win,text="1",font=("arial",20,"bold"),bd=5,width=4,bg="powderblue",command=lambda:bclick(1))
b1.place(x=0,y=260)
b2=Button(win,text="2",font=("arial",20,"bold"),bd=5,width=4,bg="powderblue",command=lambda:bclick(2))
b2.place(x=80,y=260)
b3=Button(win,text="3",font=("arial",20,"bold"),bd=5,width=4,bg="powderblue",command=lambda:bclick(3))
b3.place(x=160,y=260)
bplus=Button(win,text="+",font=("arial",20,"bold"),bd=5,fg="red",bg="powderblue",width=4,command=lambda:bclick('+'))
bplus.place(x=240,y=260)
bcbr=Button(win,text="(",font=("arial",20,"bold"),bd=5,fg="red",bg="powderblue",width=4,command=lambda:bclick('('))
bcbr.place(x=0,y=320)
b0=Button(win,text="0",font=("arial",20,"bold"),bd=5,width=4,bg="powderblue",command=lambda:bclick(0))
b0.place(x=80,y=320)
bobr=Button(win,text=")",font=("arial",20,"bold"),bd=5,fg="red",bg="powderblue",width=4,command=lambda:bclick(')'))
bobr.place(x=160,y=320)
bequal=Button(win,text="=",font=("arial",20,"bold"),bd=5,fg="red",bg="powderblue",width=4,command=bEquals)
bequal.place(x=240,y=320)


win.mainloop()
































































































