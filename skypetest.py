from time import strftime
from tkinter import *

a = strftime('%H')
def calculate():
    x = Entry(gui,text= "what hour of the day is it? ")
    y = x = input("what time is ti ")
  
    if x == a:
        print("Yes,Is is ", a , "o'clock")
    else:
        print("No, Is is ", a , "o'clock")
        print("You should keep count of date and time")
        print("better luck next time")



gui = Tk()
gui.title("What time is it?")



x = Entry(gui)

btn = Button(gui,text = "Submit!",command = lambda:())


gui.mainloop()



