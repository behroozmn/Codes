from tkinter import *
import tkinter.font as font

from matplotlib.ft2font import ITALIC

tkWnd = Tk()
tkWnd.title("button")
tkWnd.geometry('400x300')
tkWnd.resizable(width=False, height=False)
# tkWnd.configure(bg='white')
# tkWnd['bg']='green'
tkWnd['bg']='#FFFFFF'

my_name = StringVar()


def print_my_name():
    my_name.set('my name is Mohammad')

myFont = font.Font(family='Vazir',size=10, weight='bold')
btn = Button(tkWnd, text="show my name!",bg='blue',fg='red', width=20, height=1,font=myFont, command=lambda: print_my_name())
btn.place(x=10, y=10)

label = Label(tkWnd, textvariable=my_name)
label.place(x=10, y=50)

tkWnd.mainloop()
