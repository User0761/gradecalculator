from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import math
window = tk.Tk()
window.title("Grade Calculator ")
window.geometry("600x600")
window.minsize(600,600)
window.configure(bg="lightyellow")

def calc():
  global a,b,c,e,f,g,h,i,j,k,l,m,n,o,p,q,r
  a=int(str(entry.get()))
  b=int(str(entry1.get()))
  c=int(str(entry2.get()))
  d=int(str(entry3.get()))
  e=int(str(entry4.get()))
  f=int(str(entry5.get()))
  h=int(str(entry6.get()))
  l=int(str(entry7.get()))
  m=int(str(entry8.get()))
  n=int(str(entry9.get()))
  o=int(str(entry10.get()))
  p=int(str(entry11.get()))
  
  g= a + b+c+d+e+f
  lab4.configure(text=g)
  q = h + l+m+n+o+p
  tot1.configure(text=q)
  
  i=g * 100 / q
  j=float(i)
  s="{:.2f}".format(j)
  result.configure(text=s)
  if j >=91:
    k = "A1 "
    grade.configure(text=k)
  elif j>=81:
    k="A2 "
    grade.configure(text=k)
  elif j>=71:
    k="B1 "
    grade.configure(text=k)
  elif j>=61:
    k="B2 "
    grade.configure(text=k)
  elif j>=51:
    k="C1 "
    grade.configure(text=k)
  elif j>=41:
    k="C2 "
    grade.configure(text=k)
  elif j>=33:
    k="D "
    grade.configure(text=k)
  elif j<=32:
    k="E Failed "
    grade.configure(text=k)
    
    
 
  
label=Label(window,text="Grade Calculator By Devasya ",bg="lightyellow")
label.pack(side=TOP,pady=15)

label1=Label(window,text="Enter Obtained Marks",bg="lightyellow")
label1.place(x=100,y=50)

label2=Label(window,text="Science",bg="lightyellow")
label2.place(x=50,y=100)
entry=Entry(window,width=10)
entry.place(x=190,y=100)

entry6=Entry(window,width=10)
entry6.place(x=350,y=100)

label3=Label(window,text="Maths",bg="lightyellow")
label3.place(x=50,y=150)
entry1=Entry(window,width=10)
entry1.place(x=190,y=150)

entry7=Entry(window,width=10)
entry7.place(x=350,y=150)


label4=Label(window,text="English",bg="lightyellow")
label4.place(x=50,y=200)
entry2=Entry(window,width=10)
entry2.place(x=190,y=200)
entry8=Entry(window,width=10)
entry8.place(x=350,y=200)
label5=Label(window,text="S.S.T",bg="lightyellow")
label5.place(x=50,y=250)
entry3=Entry(window,width=10)
entry3.place(x=190,y=250)

entry9=Entry(window,width=10)
entry9.place(x=350,y=250)

label6=Label(window,text="Sanskrit",bg="lightyellow")
label6.place(x=50,y=300)
entry4=Entry(window,width=10)
entry4.place(x=190,y=300)
entry10=Entry(window,width=10)
entry10.place(x=350,y=300)

label7=Label(window,text="Gujarati/Hindi",bg="lightyellow")
label7.place(x=50,y=350)
entry5=Entry(window,width=10)
entry5.place(x=190,y=350)
entry11=Entry(window,width=10)
entry11.place(x=350,y=350)


tit=Label(window,text="Total Marks",bg="lightyellow")
tit.place(x=350,y=50)
tot=Label(text="Total Marks :",bg="lightyellow")
tot.place(x=350,y=400)
tot1=Label(window,bg="lightyellow")
tot1.place(x=500,y=400)


lab3=Label(window,text="You scored Marks: ",bg="lightyellow")
lab3.place(x=50,y=400)
lab4=Label(window,bg="lightyellow")
lab4.place(x=250,y=400)

cal=Button(window,text="Calculate",width=15,command=calc,bg="lightblue")
cal.place(x=200,y=450)


lab=Label(window,text="You Scored: ",bg="lightyellow")
lab.place(x=50,y=500)
lab1=Label(window,text="%",bg="lightyellow")

lab1.place(x=250,y=500)

lab2=Label(window,text="Your Grade : ",bg="lightyellow")
lab2.place(x=300,y=500)

grade=Label(window,bg="lightyellow")
grade.place(x=450,y=500)

result=Label(window,bg="lightyellow")
result.place(x=190,y=500)



tk.mainloop() 