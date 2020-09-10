import tkinter as tk

from time import strftime
gui = tk.Tk()
frame = tk.Frame(gui)
frame.pack()


a = strftime('%H')
print("Welcome")
clear = tk.Button(gui, text='Clear', fg='black', bg='red', 
                   command=calculate(), height=1, width=7) 
def main1():
    x = input("What hour of the day is it? ")
  
    if x == a:
        print("Yes,Is is ", a , "o'clock")
    else:
        print("No, Is is ", a , "o'clock")
        print("You should keep count of date and time")
        print("better luck next time")


clear = tk.Button(gui, text="let's go", fg='black', bg='red', 
                   command=calculate(), height=1, width=7) 
def button():
    button