from tkinter import *

def convert():
    kg = float(e1_value.get())
    t2.insert(END,kg*2.205)
    t3.insert(END,kg*35.274)
    t4.insert(END,kg*1000)

window = Tk()
window.title('Weight Converter')

l1= Label(window,text= "Kilograms : ")
l1.grid(row=0, column=0)

e1_value = StringVar()
e1= Entry(window,textvariable= e1_value)
e1.grid(row=0, column =1)

b1= Button(window, text= "Convert", command = convert)
b1.grid(row=0, column=3)

l2= Label(window,text= "Pounds :")
l2.grid(row=1, column=0)

t2 = Text(window, height=1, width=10)
t2.grid(row=1, column=1)

l3= Label(window,text= "Ounces :")
l3.grid(row=2, column=0)

t3 = Text(window, height=1, width=10)
t3.grid(row=2, column=1)

l4= Label(window,text= "Grams :")
l4.grid(row=3, column=0)

t4 = Text(window, height=1, width=10)
t4.grid(row=3, column=1)

window.mainloop()