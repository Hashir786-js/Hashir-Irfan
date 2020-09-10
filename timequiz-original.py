from time import strftime
a = strftime('%H')
print("Welcome")
def calculate():
    x = input("What hour of the day is it? ")
    if x == a:
        print("Yes,Is is ", a , "o'clock")
    else:
        print("No, Is is ", a , "o'clock")
        print("You should keep count of date and time")
        print("better luck next time")
calculate()
