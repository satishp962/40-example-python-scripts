from tkinter import *

root = Tk()

def red():
    root.configure(background='red')

def blue():
    root.configure(background='blue')

def green():
    root.configure(background='green')

R = Button(root, text="Red", command=red)
G = Button(root, text="Blue", command=blue)
B = Button(root, text="Green", command=green)

thelabel = Label(root, text="Click buttons to change background color")
thelabel.pack()

R.pack()
G.pack()
B.pack()
root.mainloop()