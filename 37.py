from tkinter import *

root = Tk()

def onclick():
    thelabel = Label(root, text="This is a label")
    thelabel.pack()

B = Button(root, text="Hello", command=onclick)

B.pack()
root.mainloop()