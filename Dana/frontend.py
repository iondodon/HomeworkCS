from tkinter import *
from CS_Laboratory1 import des
# from _init_ import *


# global cyphered_text

window=Tk()

window.title("Encryption Algorithms")
window.geometry('350x200')

l1=Label(window,text="The 64-bit key:",font=("Arial Bold",12))
l1.grid(row=0,column=0)

l2=Label(window,text="Text:",font=("Arial Bold",12))
l2.grid(row=1,column=0)

l3=Label(window,text="Ciphered text:",font=("Arial Bold",12))
l3.grid(row=4,column=0)

l4=Label(window, text="Dechiphered text:",font=("Arial Bold",12))
l4.grid(row=6,column=0)

#define entries

key1=StringVar()
e1=Entry(window,textvariable=key1)
e1.grid(row=0,column=1)

text1=StringVar()
e2 = Entry(window,textvariable=text1)
e2.grid(row=1,column=1)

# cyphered_text=StringVar()
# e3 = Entry(window,textvariable=cyphered_text)
# e3.grid(row=4,column=1)

#functionality

def clicked():
    key=key1.get()
    text=text1.get()
    # l5=Label(window, text=key ,font=("Arial Bold",12))
    # l5.grid(row=4,column=1)
    d = des()
    r = d.encrypt(key,text)
    l5=Label(window, text=r ,font=("Arial Bold",12))
    l5.grid(row=4,column=1)
    


     

#define buttons

b1=Button(window,text="Cypher",font=("Arial Bold",12),bg="#02cfff",command=clicked)
b1.grid(row=2,column=1)


# cyphered_text=StringVar()
# e3 = Entry(window,textvariable=cyphered_text)
# e3.grid(row=4,column=1)


window.mainloop()

