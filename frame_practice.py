import tkinter
import tkinter.ttk as tk
from tkinter import *

root = tkinter.Tk()

frame= tk.Frame(root)
frame.grid(column=0, row=0)

Button(frame, text="Open file", command=None).grid(column=0, row=1 )
Label(frame, bg='black', fg="white", text="test test test test test test ").grid(column=0, row=2 )

root.config(background="blue")
root.mainloop()