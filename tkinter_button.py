from tkinter import *

root = Tk()

# #Create Labels
# myLabel1 = Label(root, text="Hello World!")
# myLabel2 = Label(root, text="My name is John Elder")
#
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)

#Create Button

# def myClick():
#     myLabel = Label(root, text="Look I clicked the button")
#     myLabel.pack()
#
# #myButton = Button(root, text='Click Me!', state=DISABLED)
# myButton = Button(root, text='Click Me!', padx = 50, pady = 20, command = myClick)
# myButton.pack()

#Creating input Box

e = Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
e.pack()
# place text inside the input box
e.insert(0, "Enter your name")

def myClick():
    # gets input field by assigning a variable to get()
    get_input = "Hello " + e.get()
    # place get_input to text
    myLabel = Label(root, text = get_input)
    myLabel.pack()

#myButton = Button(root, text='Click Me!', state=DISABLED)
myButton = Button(root, text='Click Me!', padx = 50, pady = 20, command = myClick)
myButton.pack()


root.mainloop()

