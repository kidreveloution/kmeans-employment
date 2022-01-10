import tkinter
from tkinter import *
root = tkinter.Tk()
def click():
    entered_text = textentry.get
    print (entered_text)
window = Tk()

window.title("Davids Awesome Program")
window.configure(background = "yellow")
Label (window, text ="First, lets import your file", bg = "Yellow", fg = "black" ) . grid(row = 1, column = 0, sticky = W)

textentry = Entry(window, width = 20, bg = "white")
textentry.grid (row = 2, column = 0, sticky = W)
Button (window, text = "Submit",width = 6, command = click()).grid(row = 4)

window.mainloop()
